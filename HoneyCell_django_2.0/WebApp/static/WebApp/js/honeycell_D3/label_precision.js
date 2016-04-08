// var json_data = "";
//console.log(json_data);

// var margin = {top: 40, right: 20, bottom: 30, left: 40},
//     width = 960 - margin.left - margin.right,
//     height = 500 - margin.top - margin.bottom;

// var formatPercent = d3.format(".0%");

// var x = d3.scale.ordinal()
//     .rangeRoundBands([0, width], .1);

// var y = d3.scale.linear()
//     .range([height, 0]);

// var xAxis = d3.svg.axis()
//     .scale(x)
//     .orient("bottom");

// var yAxis = d3.svg.axis()
//     .scale(y)
//     .orient("left")
//     .tickFormat(formatPercent);

// var tip = d3.tip()
//   .attr('class', 'd3-tip')
//   .offset([-10, 0])
//   .html(function(d) {
//     return "<strong>Frequency:</strong> <span style='color:red'>" + d.frequency + "</span>";
//   })

// var svg = d3.select("body").append("svg")
//     .data(json_data)
//     .enter()
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//     .append("g")
//     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// svg.call(tip);


//   x.domain(data.map(function(d) { return d.letter; }));
//   y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

//   svg.append("g")
//       .attr("class", "x axis")
//       .attr("transform", "translate(0," + height + ")")
//       .call(xAxis);

//   svg.append("g")
//       .attr("class", "y axis")
//       .call(yAxis)
//     .append("text")
//       .attr("transform", "rotate(-90)")
//       .attr("y", 6)
//       .attr("dy", ".71em")
//       .style("text-anchor", "end")
//       .text("Frequency");

//   svg.selectAll(".bar")
//       .data(data)
//     .enter().append("rect")
//       .attr("class", "bar")
//       .attr("x", function(d) { return x(d.letter); })
//       .attr("width", x.rangeBand())
//       .attr("y", function(d) { return y(d.frequency); })
//       .attr("height", function(d) { return height - y(d.frequency); })
//       .on('mouseover', tip.show)
//       .on('mouseout', tip.hide)


// function type(d) {
//   d.frequency = +d.frequency;
//   return d;
// }


//
//var margin = {top: 20, right: 20, bottom: 30, left: 50},
//        width = 960 - margin.left - margin.right,
//        height = 500 - margin.top - margin.bottom;
//
//var parseDate = d3.time.format("%Y-%m-%d").parse; // for dates like "2014-01-01"
////var parseDate = d3.time.format("%Y-%m-%dT00:00:00Z").parse;  // for dates like "2014-01-01T00:00:00Z"
//
//var x = d3.time.scale()
//        .range([0, width]);
//
//var y = d3.scale.linear()
//        .range([height, 0]);
//
//var xAxis = d3.svg.axis()
//        .scale(x)
//        .orient("bottom");
//
//var yAxis = d3.svg.axis()
//        .scale(y)
//        .orient("left");
//
//var line = d3.svg.line()
//        .x(function (d) {
//            return x(d.month);
//        })
//        .y(function (d) {
//            return y(d.count_items);
//        });
//
//var svg = d3.select("body").append("svg")
//        .attr("width", width + margin.left + margin.right)
//        .attr("height", height + margin.top + margin.bottom)
//        .append("g")
//        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.json("/get_json_result", function (error, data) {

    console.log(data)

    //data.forEach(function (d) {
    //
    //    d.month = parseDate(d.month);
    //    d.count_items = +d.count_items;
    //});
    //
    //x.domain(d3.extent(data, function (d) {
    //    return d.month;
    //}));
    //y.domain(d3.extent(data, function (d) {
    //    return d.count_items;
    //}));
    //
    //svg.append("g")
    //        .attr("class", "x axis")
    //        .attr("transform", "translate(0," + height + ")")
    //        .call(xAxis);
    //
    //svg.append("g")
    //        .attr("class", "y axis")
    //        .call(yAxis)
    //        .append("text")
    //        .attr("transform", "rotate(-90)")
    //        .attr("y", 6)
    //        .attr("dy", ".71em")
    //        .style("text-anchor", "end")
    //        .text("Play count");
    //
    //svg.append("path")
    //        .datum(data)
    //        .attr("class", "line")
    //        .attr("d", line);


});