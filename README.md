# lotto645

무료 웹 도구 — https://phoenix1976x.github.io/lotto645/

- 🎱 **로또 6/45** — 자동·반자동(고정 번호 1~5개), 당첨금 나눠먹기 줄이기, 판매 마감 카운트다운
- 🎟️ **연금복권 720+** — 세트(1~5조)·낱장 1/5장, 조·자리별 반자동, 단순 배열 피하기
- 🔮 **토정비결·사주** — 양력/음력 생년월일 + 태어난 시간으로 토정비결 144괘(총운·12개월)와 사주 원국·오행 분포. 전부 브라우저 안에서만 계산하며 입력값을 서버로 보내거나 저장하지 않습니다.

## 파일

| 경로 | 내용 |
|---|---|
| `index.html` | 통합 페이지 (탭 3개) |
| `engines/ssaju.mjs` | 사주·만세력 엔진 (MIT © Jin, golbin/ssaju 배포 번들) |
| `engines/klc.mjs` | 음양력·간지 (MIT © Jinil Lee, korean-lunar-calendar) |
| `data/tojeong_144.json` | 토정비결 144괘 총운·월별운 원문 (MIT © Lee, JungHoon, molpass/mcp-tojeong) |
| `720/index.html` | 연금복권 720+ 단독 페이지 (초기 버전) |
| `THIRD-PARTY-LICENSES.md` | 제3자 라이선스 전문 |

토정비결 작괘식은 `mcp-tojeong`의 규칙을 그대로 옮겼습니다 — 상괘 (한국나이+태세수)÷8, 중괘 (당년 생월 날수+월건수)÷6, 하괘 (음력 생일+일진수)÷3, 나머지 0은 제수.
