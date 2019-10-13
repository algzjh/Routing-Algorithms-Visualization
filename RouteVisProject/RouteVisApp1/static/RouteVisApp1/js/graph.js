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
    console.log("start_node: \n", start_node);
    console.log("end_node: \n", end_node);

    var formdata = new FormData();
    formdata.append("id", "requestPlot");
    formdata.append("csrfmiddlewaretoken", token);
    formdata.append("start_node", start_node);
    formdata.append("end_node", end_node);
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

                var simulation = d3.forceSimulation()
                    .force("link", d3.forceLink().id(function(d) {return d.id;}))
                    .force("charge", d3.forceManyBody().strength(-4000))
                    .force("center", d3.forceCenter(width/2, height/2));

                var link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(graph_data.links)
                    .enter()
                    .append("line")
                    .attr("stroke-width", 2)
                    .style("stroke", "#aaa");

                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("g")
                    .data(graph_data.nodes)
                    .enter()
                    .append("g");

                var circles = node.append("circle")
                    .attr("r", 20)
                    .attr("fill", "#69b3a2")
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
                    link
                        .attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });

                    node
                        .attr("transform", function(d){
                            return "translate(" + d.x + "," + d.y + ")";
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

                /*
                var link = svg
                    .append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(graph_data.links)
                    .enter()
                    .append("line")
                    .attr("stroke-width", 2)
                    .style("stroke", "#aaa");

                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("g")
                    .data(graph_data.nodes)
                    .enter()
                    .append("g");

                var circles = node.append("circle")
                    .attr("r", 20)
                    .style("fill", "#69b3a2");

                var labels = node.append("text")
                    .text(function(d) {return d.name;})
                    .attr("x", 6)
                    .attr("y", 3);

                node.append("title")
                    .text(function(d) {return d.id;});


                var simulation = d3.forceSimulation(graph_data.nodes)
                    .force("links", d3.forceLink()
                            .distance(function(d) { return d.weight; })
                            .id(function(d) { return d.id; })
                            .links(graph_data.links)
                    )
                    .force("charge", d3.forceManyBody().strength(-4000))
                    .force("center", d3.forceCenter(width/2, height/2))
                    .alphaDecay(0.2)
                    .on("end", ticked);

                function ticked() {
                    link
                        .attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });

                    node
                        .attr("cx", function(d) { return d.x+6; })
                        .attr("cy", function(d) { return d.y-6; });
                }
                 */

                /*
                force.nodes(graph_data.nodes)
                    .links(graph_data.links)z`
                    .size([w, h])
                    .linkDistance([50])
                    .charge([-100])
                    .start();
                var edges = svg.selectAll("line")
                    .data(graph_data.links)
                    .enter()
                    .append("line")
                    .style("stroke", "#ccc")
                    .style("stroke-width", 1);
                var nodes = svg.selectAll("circle")
                    .data(graph_data.nodes)
                    .enter()
                    .append("circle")
                    .attr("r", 10)
                    .style("fill", function(d, i){
                        return colors(i);
                    })
                    .call(force.drag);
                force.on("tick", function(){
                    edges.attr("x1", function(d) {return d.source.x;})
                        .attr("y1", function(d) {return d.source.y;})
                        .attr("x2", function(d) {return d.target.x;})
                        .attr("y2", function(d) {return d.target.y;})
                    nodes.attr("cx", function(d) {return d.x;})
                        .attr("cy", function(d) {return d.y;})
                })
                 */
            },
            error: function (data) {
                alert("ajax Exception!!!");
            }
        }
    );
}