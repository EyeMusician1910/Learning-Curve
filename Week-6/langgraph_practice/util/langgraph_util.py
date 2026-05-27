from langchain_core.runnables.graph import MermaidDrawMethod
from PIL import Image
from io import BytesIO


def display(runnable):
    # Use xray to visualize conditional edges (dashed lines) and routing.
    graph_image = runnable.get_graph(xray=True).draw_mermaid_png(
        draw_method=MermaidDrawMethod.API,
        output_file_path="../graph.png"
    )
    img = Image.open(BytesIO(graph_image))
    img.show()
