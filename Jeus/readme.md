# Jeus App Documentations

Jeus Django App 정의 문서

## 정의
---
Jeus Django App 은 기업내의 조직도 관리 및 사원에 대한 정보 관리 기능을 통해, Artemis 프로젝트가 지향하는 전사적 관리 프로젝트에 기여한다.
Jeus 앱은 단순히 하나의 회사가 아닌 여러 계열사를 가진 회사들의 조직을 관리하며, 이를 기반으로 통합 솔루션 기능을 제공할 수 있다.

## 모델 정의
---
JsCompany Model

예스이십사 주식회사

* company\_name
* company\_ci - image
* company\_master - ForeignKey\(Auth.Users\)
* company\_telephone
* company\_description

JsDivision Model

IT사업본부

* division\_name
* division\_master - ForeignKey\(Auth.Users\)
* division\_ci - Image
* division\_telephone
* division\_description

JsTeam Model

인프라운영팀

* team\_name
* team\_master - ForeignKey\(Auth.Users\)
* team\_ci - image
* team\_telephone
* team\_description

JsPart Model

시스템보안파트

* part\_name
* part\_master - ForeignKey\(Auth.Users\)
* part\_ci - image
* part\_telephone
* part\_description

JsUser Model

* jsuser - OneToOneField\(django.contrib.auth.models.User, on\_delete=model.CASCADE\)
* user\_company - Yes24주식회사
* user\_division - IT 사업본부
* user\_part - 시스템보안파트
* user\_telephone - 010-5598-4457
* user\_birthday - 1988-12-12
* user\_rank/position \(직급\) - ForeignKey\(Jeus.models.JsRank\)
* user\_description \(담당 직무: 보안성 검토, 침해사고 대응, 악성코드 분석/차단, 기타 보안 이슈 관리, 개발\)

JsRank Model

사원\(=1\)

* rank\_name
* rank\_grade - Integer \(JsRankEnum.Staff = 1, JsRankEnum.AssistantManager = 2, .... \)

JsTask Model \(Node\)

보안성 검토

* task\_name - 기술적 보안성검토 요청
* task\_type - 보안성 검토 \(?\)
* task\_user - ForeignKey\(JsUser\)
* task\_start - datetime
* task\_end - datetime

JsLink Model \(Link\)

* work\_instance - ForeignKey\(JsWork\)
* link\_name - 보안성 검토 프로젝트 전달
* forward\_task - ForeignKey\(JsTask\), 취약점 조치
* backword\_task - ForeignKey\(JsTask\), 보안성 검토

JsWork Model

* work\_number
* work\_title - 2017년도 OO 사이트 리마스터링 프로젝트 
* work\_start 
* work\_end

## Model Simulation

**CASE A. **

> 시스템개발파트 이모모 대리는 김모모 사원에게 프로젝트 개발 완료 후 보안성 검토를 요청하려고 한다.

객체 정의

시스템개발파트 :JsDivision

이모모 : JsUser

대리 : JsUser.user\_rank \(JsRank\)

김모모 :  JsUser

사원 : JsUser.user\_rank \(JsRank\)

보안성 검토 : 할당된 직무

관계 1

상위 관계 : 대리 &gt; 사원

## Extending Django User Model
---
### 참고

* [원문 사이트 \(simpleisbetterthancomplex.com\)](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)



