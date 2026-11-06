const API_URL = "https://benji-kmeans-backend.onrender.com";

const graph = document.getElementById("graph");
const ctx = graph.getContext("2d");
const statusText = document.getElementById("status");
const deleteButton = document.getElementById("delete");
const clusterButton = document.getElementById("cluster");
const clusterCount = document.getElementById("cluster_count");

const colors = [
    "#2563eb", "#dc2626", "#15803d", "#7e22ce", "#c2410c",
    "#0e7490", "#be185d", "#4d7c0f", "#854d0e", "#475569",
];

const points = [];
let result = null;
let maxPoints = 1000;
let pendingRequest = null;

function drawPoints(message = "") {
    ctx.clearRect(0, 0, graph.width, graph.height);

    points.forEach((point, index) => {
        const label = result?.labels[index] ?? 0;

        ctx.beginPath();
        ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
        ctx.fillStyle = colors[label];
        ctx.fill();
    });

    result?.centers.forEach((center, index) => {
        ctx.fillStyle = colors[index];
        ctx.fillRect(center.x - 6, center.y - 6, 12, 12);
        ctx.strokeStyle = "#111827";
        ctx.strokeRect(center.x - 6, center.y - 6, 12, 12);
    });

    statusText.textContent = `Broj točaka: ${points.length}`;
    if (message) {
        statusText.textContent += ` · ${message}`;
    }
}

function resetGrouping() {
    pendingRequest?.abort();
    result = null;
    drawPoints();
}

async function loadConfig() {
    try {
        const response = await fetch(`${API_URL}/api/config`);
        if (!response.ok) {
            throw new Error("Postavke nisu dostupne.");
        }

        const config = await response.json();
        clusterCount.min = config.min_clusters;
        clusterCount.max = config.max_clusters;
        maxPoints = config.max_points;
    } catch {
        if (points.length === 0 && !pendingRequest) {
            drawPoints("Postavke API-ja nisu dostupne. Možeš pokušati grupirati točke.");
        }
    }
}

graph.addEventListener("click", (event) => {
    const rect = graph.getBoundingClientRect();
    const x = (event.clientX - rect.left - graph.clientLeft)
        * graph.width / graph.clientWidth;
    const y = (event.clientY - rect.top - graph.clientTop)
        * graph.height / graph.clientHeight;

    if (x < 0 || x > graph.width || y < 0 || y > graph.height) {
        return;
    }
    if (points.length >= maxPoints) {
        drawPoints(`Možeš dodati najviše ${maxPoints} točaka.`);
        return;
    }

    points.push({ x, y });
    resetGrouping();
});

deleteButton.addEventListener("click", () => {
    points.length = 0;
    resetGrouping();
});

clusterCount.addEventListener("input", resetGrouping);

clusterButton.addEventListener("click", async () => {
    const k = clusterCount.valueAsNumber;

    if (!Number.isInteger(k) || !clusterCount.checkValidity()) {
        drawPoints(`Upiši cijeli broj grupa od ${clusterCount.min} do ${clusterCount.max}.`);
        return;
    }
    if (points.length < k) {
        drawPoints(`Dodaj najmanje ${k} točaka.`);
        return;
    }

    const controller = new AbortController();
    pendingRequest = controller;
    clusterButton.disabled = true;
    result = null;
    drawPoints("Grupiranje u tijeku…");

    try {
        const response = await fetch(`${API_URL}/api/cluster`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ k, points }),
            signal: controller.signal,
        });

        const data = await response.json();

        if (controller.signal.aborted) {
            return;
        }
        if (!response.ok) {
            throw new Error(
                typeof data.detail === "string" ? data.detail : "Grupiranje nije uspjelo."
            );
        }

        result = data;
        drawPoints(`Broj grupa: ${new Set(data.labels).size}`);
    } catch (error) {
        if (!controller.signal.aborted) {
            const message = error instanceof TypeError
                ? "Povezivanje s API-jem nije uspjelo."
                : error.message;
            drawPoints(message);
        }
    } finally {
        pendingRequest = null;
        clusterButton.disabled = false;
    }
});

loadConfig();