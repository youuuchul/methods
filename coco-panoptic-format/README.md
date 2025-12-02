# COCO Panoptic Format & ID Encoding

본 폴더는 **Panoptic Segmentation**의 개념과  
COCO 공식 포맷(COCO Panoptic Format)의 category 구조,  
그리고 panoptic mask 저장 시 사용되는 **RGB ↔ panoptic_id 인코딩 방식**을 정리

---

## 🧩 1. Panoptic Segmentation 개념

Panoptic Segmentation은 **Semantic Segmentation**과 **Instance Segmentation**을 통합한 기법

- **Semantic Segmentation**  
  각 픽셀마다 ‘어떤 클래스인지’만 예측  
  (예: 사람/길/나무/하늘)

- **Instance Segmentation**  
  동일 클래스 내에서 개별 객체까지 구분  
  (예: 사람 #1, 사람 #2, 사람 #3)

- **Panoptic Segmentation**  
  모든 픽셀에 대해  
  - 어떤 클래스(class_id)
  - 어떤 인스턴스(instance_id)  
  를 동시에 제공하는 세그멘테이션 방식

각 픽셀은 일반적으로 `(class_id, instance_id)`를 가지며,  
이를 하나의 정수값인 **panoptic_id**로 인코딩하기도 함

---

## 📦 2. COCO Panoptic JSON 구조

COCO panoptic format의 `categories`는 다음 정보를 포함

- `id` : 고유 category_id  
- `name` : 클래스 이름  
- `supercategory` : 상위 그룹  
- `isthing` : thing(객체) 구분 여부  
- `color` : panoptic mask에서 RGB로 사용되는 색 (0~255 3채널)

예시(JSON 일부):

```json
{
  "id": 1392804,
  "name": "Ball",
  "supercategory": "Ball",
  "isthing": 1,
  "color": [164, 64, 21]
}