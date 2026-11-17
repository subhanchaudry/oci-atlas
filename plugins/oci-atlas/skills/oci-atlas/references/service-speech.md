# Speech transcription and realtime voice output

Reviewed: 2026-11-17

## Choose the direction and latency

Use transcription to turn audio into text and text-to-speech (TTS) to produce audio. Batch transcription jobs process input media and write results to Object Storage; live transcription uses a streaming interaction. Realtime TTS accepts incremental text and returns audio through a WebSocket API. It is API-only in the November release; a batch job or Console screen is not an interchangeable interface.

## Prerequisites

Identify language, model/voice, media format, sample rate, latency and output requirements. Verify feature-specific regional availability: the reviewed Speech overview restricts TTS to US West (Phoenix), even though transcription has broader commercial-region coverage. Confirm the chosen endpoint before sending data.

Separate permission to submit work from access to input and output objects. Resolve the service/runtime principal and required policies; a readable bucket in an operator's session does not prove that the service can process it. Keep application authentication material outside source and logs.

## Working pattern

1. Select **Speech** in the Console for supported job operations, or use the owning SDK/API for the chosen streaming feature. Inspect current limits and supported request fields.
2. For batch transcription, identify exact input objects, output prefix and options, submit a bounded job, and inspect every task result. Retain job/task IDs with source object versions.
3. Review transcript timestamps and representative passages against the audio. Speaker labels are diarization output, not verified personal identities. Noise, overlap and language changes can affect accuracy.
4. For realtime TTS, establish the authenticated WebSocket session using the documented protocol, send incremental text and consume audio in order. Test cancellation, disconnect handling and application buffering; replaying text after reconnection can repeat audible output.
5. Verify the result in the consuming application before increasing volume or connecting a downstream search/agent workflow.

## Retention and operating cost

Track processed audio/text usage, retained recordings/transcripts and downstream storage or model calls using current pricing. A finished or canceled job does not remove its input or output objects. Set appropriate retention for each artifact and close streaming sessions when the application no longer needs them. Use [event processing](recipe-event-processing.md) for idempotent processing of uploaded recordings and [RAG](recipe-rag-application.md) only when authorized transcripts need retrieval.

## Sources

- [Speech capabilities, regional restrictions and jobs](https://docs.oracle.com/en-us/iaas/Content/speech/using/speech.htm)
- [Realtime TTS API availability](https://docs.oracle.com/en-us/iaas/releasenotes/speech/realtime-tts.htm)
