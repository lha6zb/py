import requests

@app.get("/stream_online")
async def stream_online_video():
    video_url = "https://example.com/video.mp4"  # 替换为实际视频 URL
    
    response = requests.get(video_url, stream=True)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error: {response.status_code}"
        )
    
    return StreamingResponse(
        response.iter_content(chunk_size=1024 * 1024),  # 1MB chunks
        media_type="video/mp4"
    )