function onClickGenerateGraph(){
    let dataset = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95];
    console.log("dataset: \n", dataset);
    d3.select('#graph-area').select('svg').remove();


    var margin = {top: 10, right: 30, bottom: 30, left: 40};
    width -= margin.left + margin.right;
    height -= margin.top + margin.bottom;
    var colors = d3.scaleOrdinal(d3.schemeCategory10);

    var svg = d3.select("#graph-area")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
        //.append("g");

    // 1424 731


    let start_node = document.getElementById("start-node").value;
    let end_node = document.getElementById("end-node").value;
    let alg_name = document.getElementById("algorithm-selector").value;
    let data_source_name = document.getElementById("data-source-selector").value;
    console.log("start_node: \n", start_node);
    console.log("end_node: \n", end_node);
    console.log("alg_name: \n", alg_name);

    var formdata = new FormData();
    formdata.append("id", "requestPlot");
    formdata.append("csrfmiddlewaretoken", token);
    formdata.append("start_node", start_node);
    formdata.append("end_node", end_node);
    formdata.append("alg_name", alg_name);
    formdata.append("data_source_name", data_source_name);
    console.log("formdata: \n", formdata);

    $.ajaxSetup({
        data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
    });

    $.ajax(
        {
            url: "http://127.0.0.1:8000/RouteVisApp1/",
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false,
            success:function(data){
                jsondata = $.parseJSON(data);

                graph_data = jsondata.graph_data;
                console.log("graph_data: \n", graph_data);

                var my_strength = -4000;
                if(data_source_name==="1"){
                    my_strength = -500
                }
                var circle_radius = 20;

                var simulation = d3.forceSimulation()
                    .force("link", d3.forceLink().id(function(d) {return d.id;}))
                    .force("charge", d3.forceManyBody().strength(my_strength))
                    .force("center", d3.forceCenter(width/2, height/2));

                // var link = svg.append("g")
                //     .attr("class", "links")
                //     .selectAll("line")
                //     .data(graph_data.links)
                //     .enter()
                //     .append("line")
                //     .attr("stroke-width", 2)
                //     .style("stroke", "#aaa");

                var link = svg.selectAll(".link")
                    .data(graph_data.links)
                    .enter()
                    .append("g")
                    .attr("class", "link")
                    .append("line")
                    .attr("class", "link-line")
                    .attr("stroke-width", 4)
                    .style("stroke", "#aaa");


                var linkText = svg.selectAll(".link")
                    .append("text")
                    .attr("class", "link-label")
                    .attr("fill", "Black")
                    .attr("dy", ".35em")
                    .attr("text-anchor", "middle")
                    .text(function(d) {return d.weight;});

                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("g")
                    .data(graph_data.nodes)
                    .enter()
                    .append("g");

                var circles = node.append("circle")
                    .attr("r", circle_radius)
                    .attr("fill", "#69b3a2")
                    .attr("id", function(d) {return "circle-" + d.name;})
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));

                var labels = node.append("text")
                    .text(function(d) {return d.name;})
                    .attr("x", -10)
                    .attr("y", 5);

                node.append("title")
                    .text(function(d) {return d.name;});

                simulation
                    .nodes(graph_data.nodes)
                    .on("tick", ticked);

                simulation.force("link")
                    .links(graph_data.links);

                function ticked() {
                    node
                        .attr("transform", function(d){
                            // return "translate(" + d.x + "," + d.y + ")";
                            return "translate(" + Math.max(circle_radius, Math.min(width - circle_radius, d.x)) + "," +
                                                  Math.max(circle_radius, Math.min(height - circle_radius, d.y)) + ")";
                        });

                    link
                        .attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });


                    linkText
                        .attr("x", function(d){
                            return ((d.source.x + d.target.x)/2);
                        })
                        .attr("y", function(d){
                            return ((d.source.y + d.target.y)/2);
                        })
                }

                function dragstarted(d) {
                  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
                  d.fx = d.x;
                  d.fy = d.y;
                }

                function dragged(d) {
                  d.fx = d3.event.x;
                  d.fy = d3.event.y;
                }

                function dragended(d) {
                  if (!d3.event.active) simulation.alphaTarget(0);
                  d.fx = null;
                  d.fy = null;
                }

            },
            error: function (data) {
                alert("ajax Exception!!!");
            }
        }
    );
}