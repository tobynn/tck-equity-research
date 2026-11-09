# [실적 공시 자동 갱신]

매 영업일 한국시간 오전 8시 20분에 GitHub Actions가 DART를 조회한다. 대상은 사업보고서·반기보고서·분기보고서·영업(잠정)실적 공시다. 새 접수번호를 찾으면 `data/disclosure_watch.json`과 `report/DISCLOSURE_UPDATE_LOG.md`를 자동으로 갱신하고 커밋한다.

이 작업은 공시의 접수와 원문 링크를 기록한다. 실제 재무제표 수치, 실적 전망, DCF·RIM·PER, 투자의견과 목표주가는 공시 원문과 회사 IR 자료를 대조한 뒤 수정한다. 자동 감지 결과만으로 가정이나 목표주가를 바꾸지 않는다.

작동을 시작하려면 저장소 Settings → Secrets and variables → Actions에서 `DART_API_KEY`를 등록한다. 키는 OpenDART에서 발급받는다. 키는 코드·커밋·로그에 기록되지 않는다.

수동 실행은 Actions 탭의 `DART earnings disclosure watch`에서 `Run workflow`를 누르면 된다. 실행 결과가 새 공시를 찾지 못하면 커밋을 만들지 않는다.
