import asyncio
import websockets
import json
import numpy as np
import cv2
from datetime import datetime

async def handle_video_stream(websocket, path):
    client_id = id(websocket)  # 각 클라이언트 연결에 고유 ID 부여
    print(f"새로운 클라이언트 연결됨 (ID: {client_id})")
    frame_count = 0
    
    try:
        while True:
            # 클라이언트로부터 데이터 수신
            data = await websocket.recv()
            frame_count += 1
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # JSON 데이터 파싱
            message = json.loads(data)
            metadata = message['metadata']
            image_data = message['imageData']
            
            print(f"[{current_time}] 클라이언트 {client_id}로부터 프레임 {frame_count} 수신")
            print(f"이미지 크기: {metadata['width']}x{metadata['height']}")
            print(f"데이터 크기: {len(image_data)} bytes")
            
            # 이미지 재구성
            width = metadata['width']
            height = metadata['height']
            
            # YUV 데이터를 numpy 배열로 변환
            yuv_data = np.frombuffer(bytes(image_data), dtype=np.uint8)
            
            try:
                # YUV를 BGR로 변환
                frame = cv2.cvtColor(
                    yuv_data.reshape((height * 3 // 2, width)), 
                    cv2.COLOR_YUV2BGR_NV21
                )
                
                # 이미지 저장 (옵션)
                cv2.imwrite(f'received_frame_{frame_count}.jpg', frame)
                print(f"프레임 {frame_count} 저장 완료")
                
            except Exception as e:
                print(f"이미지 변환 중 오류 발생: {e}")
            
            # 처리 결과를 클라이언트에게 전송
            await websocket.send("프레임 처리 완료")
            
    except websockets.exceptions.ConnectionClosed:
        print(f"클라이언트 {client_id} 연결 종료")
    except Exception as e:
        print(f"에러 발생: {e}")

async def main():
    server = await websockets.serve(
        handle_video_stream,
        "localhost",
        8000
    )
    print("비디오 스트리밍 서버가 시작되었습니다.")
    print("localhost:8000에서 연결 대기 중...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main()) 