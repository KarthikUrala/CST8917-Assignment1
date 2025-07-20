import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    input_data = context.get_input()
    metadata = yield context.call_activity("ExtractMetadataActivity", input_data)
    yield context.call_activity("StoreMetadataActivity", metadata)
    return "Metadata processed."

main = df.Orchestrator.create(orchestrator_function)
