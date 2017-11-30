$(document).ready( function() {
  $('#submit-button').click(function (e) {
    $('#word-cloud').empty();

    $.post('/', { url: $('#url').val() }).done(function (response) {
      var data = JSON.parse(response);
      var frequency_list = [];
      var max_size = 0;
      for (var k in data) {
        if (max_size === 0) {
          max_size = data[k];
        }

        var size = (data[k] * 100) / max_size;
        frequency_list.push( {"text": k, "size": size });
      }

      var color = d3.scale.linear()
              .domain([0,1,2,3,4,5,6,10,15,20,100])
              .range(["#FF1425", "#FF7216", "#BB1425", "#8B4500",
                "#991425", "#EED5B7", "#551425", "#8B8378", "#A0522D",
                "#CD6839", "#A52A2A", "##CD9B9B"]);

      d3.layout.cloud().size([800, 300])
              .words(frequency_list)
              .rotate(0)
              .fontSize(function(d) { return d.size; })
              .on("end", draw)
              .start();

      function draw(words) {
        d3.select("#word-cloud").append("svg")
                .attr("width", 850)
                .attr("height", 350)
                .attr("class", "wordcloud")
                .append("g")
                .attr("transform", "translate(320,200)")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("fill", function(d, i) { return color(i); })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function(d) { return d.text; });
      }
    })
  });
});