# 제3자 오픈소스 고지 (Third-Party Licenses)

이 페이지(`https://phoenix1976x.github.io/lotto645/`)의 `🔮 토정비결·사주` 탭은
아래 MIT 라이선스 오픈소스를 그대로(또는 브라우저용 빌드 그대로) 사용합니다.
모든 계산은 방문자의 기기(브라우저) 안에서만 이루어지며, 입력한 생년월일은 어디로도 전송되지 않습니다.

---

## 1. ssaju — 사주·만세력 엔진

- 저장소: https://github.com/golbin/ssaju
- npm: https://www.npmjs.com/package/ssaju (v0.2.0)
- 사용 파일: `engines/ssaju.mjs` (저장소가 배포하는 ESM 번들 그대로)
- 용도: 사주 원국(연주·월주·일주·시주), 오행 분포, 십성, 12운성, 음양력 변환

```
MIT License

Copyright (c) 2026 Jin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 2. mcp-tojeong — 토정비결 144괘 작괘·원문 데이터

- 저장소: https://github.com/molpass/mcp-tojeong
- 사용 파일: `data/tojeong_144.json` (저장소의 `data/tojeong_144.json`을 그대로, 공백만 제거)
- 사용한 계산 규칙: `src/calc.js`(상·중·하괘 작괘), `src/ganji.js`(태세수·월건수·일진수 조견표)를
  브라우저용 JavaScript로 옮겨 사용 (계산식·수표 동일)

```
MIT License

Copyright (c) 2026 Lee, JungHoon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 3. korean-lunar-calendar — 음양력 변환·간지

- npm: https://www.npmjs.com/package/korean-lunar-calendar (v0.4.0)
- 사용 파일: `engines/klc.mjs` (패키지가 배포하는 ESM 빌드 그대로)
- 용도: 양력↔음력 변환, 음력 월의 날수(대월 30·소월 29), 연·월·일 간지(干支)

```
MIT License

Copyright (c) 2022 Jinil Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 토정비결 원문 데이터에 대하여

144괘의 총운·월별운 원문은 `mcp-tojeong` 저장소가 MIT 라이선스로 배포하는
`data/tojeong_144.json`을 그대로 사용했습니다(개인 소장 자료(1998)를 현대 맞춤법으로
윤문한 것이라고 저장소가 밝히고 있습니다). 원문의 저작권 귀속에 문제가 있다고 판단되면
연락 주시면 해당 데이터를 즉시 내리겠습니다.

토정비결은 조선 후기부터 이어진 세시풍속(歲時風俗)으로, 이 페이지가 보여 주는 운세는
재미·참고용 전통 텍스트이며 미래를 예측하거나 보장하지 않습니다(과학적 사실 아님·운명론 아님).
중요한 의사결정의 근거로 삼지 마세요.
