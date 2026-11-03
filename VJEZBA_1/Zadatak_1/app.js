const graph = document.getElementById("graph");
const ctx = graph.getContext("2d");
const statusText = document.getElementById("status");
const deleteButton = document.getElementById("delete");

const points = [];

function drawPoints() {
    ctx.clearRect(0, 0, graph.width, graph.height);

    for (const point of points) {
        ctx.beginPath();
        ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
        ctx.fillStyle = "#2563eb";
        ctx.fill();
    }

    statusText.textContent = `Broj točaka: ${points.length}`;
}

graph.addEventListener("click", (event) => {
    const rect = graph.getBoundingClientRect();

    const x = (event.clientX - rect.left - graph.clientLeft)
        * graph.width / graph.clientWidth;

    const y = (event.clientY - rect.top - graph.clientTop)
        * graph.height / graph.clientHeight;

    points.push({ x, y });
    drawPoints();
});

deleteButton.addEventListener("click", () => {
    points.length = 0;
    drawPoints();
});