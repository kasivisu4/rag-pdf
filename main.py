import logging
from fastapi import FastAPI
import uvicorn
import inngest
import inngest.fast_api
from inngest.experimental import ai
import uuid
import os
import datetime

from dotenv import load_dotenv

load_dotenv()

inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer(),
)


@inngest_client.create_function(
    fn_id="RAG: Ingest PDF", trigger=inngest.TriggerEvent(event="rag/ingest_pdf")
)
async def rag_ingest_pdf(ctx: inngest.Context):
    return {"gh": "tmrw"}


app = FastAPI()


inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf])
