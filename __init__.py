import logging
import azure.functions as func
import azure.durable_functions as df

async def main(blob: func.InputStream, starter: str):
    client = df.DurableOrchestrationClient(starter)
    input_data = {
        "blob_name": blob.name
    }
    instance_id = await client.start_new("OrchestratorFunction", None, input_data)
    logging.info(f"Started orchestration with ID = '{instance_id}'.")
