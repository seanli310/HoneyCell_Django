
var margin = {top: 20, right: 20, bottom: 30, left: 80},
    width = 700 - margin.left - margin.right,
    height = 350 - margin.top - margin.bottom;

var formatPercent = d3.format(".0%");

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1, 1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(formatPercent);

var tip = d3.tip()
      .attr('class', 'd3-tip')
      .direction('n')
      .offset([-10, 2])
      .html(function(d) {
        return "<strong>Precision:</strong> <span style='color:red'>" + 
                d.Precision + "</span>";
    });

var svg = d3.select("#label_precision")
	  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);



var task_id = document.getElementById("task_id").value;

d3.json("/get_json_result/" + task_id, function(error, json_data) {

  // console.log(json_data);
  json_data = JSON.parse(json_data);

  var label_num = json_data.LabelNum;
  var data = [];

  for (var i = 0; i < label_num; i++) {
      data[i] = {Labels: i, Precision: json_data.Labels[i].Precision};
    console.log(data[i]);
  }

  // console.log(data);

  data.forEach(function(d) {
    // console.log(d.Precision);
    d.Precision = +d.Precision;
  });

  x.domain(data.map(function(d) { return d.Labels; }));
  y.domain([0, d3.max(data, function(d) { return d.Precision; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Precision");

  svg.selectAll(".precision_bar")
      .data(data)
      .enter()
      .append("rect")
      .attr("class", "precision_bar")
      .attr("x", function(d) { return x(d.Labels); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.Precision); })
      .attr("height", function(d) { return height - y(d.Precision); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)
      ;

  d3.select("#precison_sort").on("change", change);

  var sortTimeout = setTimeout(function() {
    d3.select("#precison_sort").property("checked", true).each(change);
  }, 2000);

  function change() {
    clearTimeout(sortTimeout);

    // Copy-on-write since tweens are evaluated after a delay.
    var x0 = x.domain(data.sort(this.checked
        ? function(a, b) { return b.Precision - a.Precision; }
        : function(a, b) { return d3.ascending(a.Labels, b.Labels); })
        .map(function(d) { return d.Labels; }))
        .copy();

    svg.selectAll(".precision_bar")
        .sort(function(a, b) { return x0(a.Labels) - x0(b.Labels); });

    var transition = svg.transition().duration(750),
        delay = function(d, i) { return i * 50; };

    transition.selectAll(".precision_bar")
        .delay(delay)
        .attr("x", function(d) { return x0(d.Labels); });

    transition.select(".x.axis")
        .call(xAxis)
      .selectAll("g")
        .delay(delay);
  }
});
