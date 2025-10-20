import json
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="hello")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    body = {"message": "Hello from Azure Functions!"}
    return func.HttpResponse(
        json.dumps(body),
        mimetype="application/json",
        status_code=200
    )

