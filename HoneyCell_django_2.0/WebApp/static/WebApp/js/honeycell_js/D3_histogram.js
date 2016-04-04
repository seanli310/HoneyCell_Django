
var w = 500;
var h = 400;

var dataset = [ 
    { key: 0, value: 0.8095 },
    { key: 1, value: 1.0 },
    { key: 2, value: 0.7895 }
    ];

var xScale = d3.scale.ordinal()
                .domain(d3.range(dataset.length))
                .rangeRoundBands([0, w], 0.05); 

var yScale = d3.scale.linear()
                .domain([0, d3.max(dataset, function(d) {return d.value;})])
                .range([0, h]);

var tip = d3.tip()
      .attr('class', 'd3-tip')
      .direction('e')
      .offset([0, 20])
      .html(function(d) {
        // return '<table id="tiptable">' + d.value + "</table>";
        return "<strong>Precision:</strong> <span style='color:red'>" + d.value + "</span>";
    });


var key = function(d) {
    return d.key;
};

//Create SVG element
var svg = d3.select("label-precision-chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

svg.call(tip);




//Create bars
svg.selectAll("rect")
   .data(dataset, key)
   .enter()
   .append("rect")
   .attr("x", function(d, i) {
        return xScale(i);
   })
   .attr("y", function(d) {
        return h - yScale(d.value);
   })
   .attr("width", xScale.rangeBand())
   .attr("height", function(d) {
        return yScale(d.value);
   })
   .attr("fill", function(d) {
        return "rgb(0, 0, " + (d.value * 5000) + ")";
   })

    //Tooltip
    .on("mouseover", function(d) {
        //Get this bar's x/y values, then augment for the tooltip
        var xPosition = parseFloat(d3.select(this).attr("x")) + xScale.rangeBand() / 2;
        var yPosition = parseFloat(d3.select(this).attr("y")) + 14;
        
        //Update Tooltip Position & value
        d3.select("#tooltip")
            .style("left", xPosition + "px")
            .style("top", yPosition + "px")
            .select("#value")
            .text("lallalal");
        d3.select("#tooltip").classed("hidden", false);
        
    })
    .on('mouseover', tip.show)
    .on("mouseout", function() {
        //Remove the tooltip
        d3.select("#tooltip").classed("hidden", true);
    })  
    .on('mouseout', tip.hide)
    ;

//Create labels
svg.selectAll("text")
   .data(dataset, key)
   .enter()
   .append("text")
   .text(function(d) {
        return "Label: " + d.key;
   })
   .attr("text-anchor", "middle")
   .attr("x", function(d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
   })
   .attr("y", function(d) {
        return h - yScale(d.value) + 14;
   })
   .attr("font-family", "sans-serif") 
   .attr("font-size", "11px")
   .attr("fill", "white");
   
var sortOrder = false;
var sortBars = function () {
    sortOrder = !sortOrder;
    
    sortItems = function (a, b) {
        if (sortOrder) {
            return a.value - b.value;
        }
        return b.value - a.value;
    };

    svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return "Label: " + d.key;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
};

// Add the onclick callback to the button
d3.select("#sort").on("click", sortBars);
d3.select("#reset").on("click", reset);

function randomSort() {

    svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.value;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
}

function reset() {
    svg.selectAll("rect")
        .sort(function(a, b){
            return a.key - b.key;
        })
        .transition()
        .delay(function (d, i) {
        return i * 50;
        })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
        });
        
    svg.selectAll('text')
        .sort(function(a, b){
            return a.key - b.key;
        })
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return "Label: " + d.key;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
};
 
    


