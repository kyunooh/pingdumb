# Pingdumb 프로젝트 소개
<h2>Pingdumb이름에서 부터 느껴지는 카피캣 냄새</h2>

<p>Pingdom이라는 서비스를 알고 계신 분들이라면 다들 눈치 채셨겠지만,</p>

<p>사이트 상태를 체크하기 위해 만든 프로젝트입니다.</p>

<p>사실 실제 Pingdom에서 제공하는 서비스는 단순 페이지 상태의 체크 뿐만이 아니라</p>

<p>다양한 기능을 제공하지만, 개인 이용자에게는 사실 그렇게 많은 기능들은 필요 없죠.</p>

<p>그래서 Pingdom을 대체할만한 무료서비스를 찾아봤지만 따로 나오는 게 없어서</p>

<p>사이트 응답값만 체크하는 간단한 프로젝트로,&nbsp;직접 만들게 되었습니다.</p>

<p>빠르게 프로토타입을 만들고 나니 점점 욕심이 생겨서 프로젝트를 발전 시켜 나가고 있습니다.</p>

<h3>사용방법</h3>

<p>프로젝트를 복사한 뒤&nbsp;</p>
<code><pre>python pingdumb.py
URL to test? (http://jellyms.kr)
Receive mail? (chm073@gmail.com)
SMTP server? (smtp.gmail.com:587)
SMTP Server username? (jellymsblog)
SMTP Server password?
interval of seconds? (300)</pre></code>
<p>위와 같이 콘솔로 값을 설정해 주시면 200(OK)이 아닐경우에 메일을 보내도록 구현하였습니다.</p>

<p>기본 설정값에서 패스워드만 입력하고 싶을때는 p 옵션을 주면 됩니다.</p>
<code><pre>python pingdumb.py -p
SMTP Server password?</pre></code>

<h4>개선해야 할 점</h4>

<p>응답코드 범위를 유저가 설정 가능하도록 함</p>

<p>pypi 에 등록하기</p>

<p>테스트 코드와 실제 구동코드 모듈 분리</p>

<p>그외 기타 오류</p>
