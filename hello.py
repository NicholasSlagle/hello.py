<!DOCTYPE html>
<!-- saved from url=(0047)https://repl.it/@MateoMugen/SoggyKnobbyProducts -->
<html lang="en" class=" "><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title class="next-head">Repl.it - SoggyKnobbyProducts</title><link rel="shortcut icon" href="https://repl.it/public/images/favicon.ico" type="image/vnd.microsoft.icon" class="next-head"><meta property="og:description" content="Powerful and simple online compiler, IDE, interpreter, and REPL. Code, compile, and run code in 30+ programming languages: Clojure, Haskell, Kotlin (beta), QBasic, Forth, LOLCODE, BrainF, Emoticon, Bloop, Unlambda, JavaScript, CoffeeScript, Scheme, APL, Lua, Python 2.7, Ruby, Roy, PHP, Python, Nodejs, Enzyme, Go, Java, C++, C++11, C, C#, F#, HTML, CSS, JS, Rust, Swift, Python (with Turtle), Jest, Django, Express, Sinatra, Ruby on Rails, R, Next.js, GatsbyJS, React, React Typescript, React Reason, bash, Quil" class="next-head"><meta property="og:type" content="article" class="next-head"><meta property="og:site_name" content="repl.it" class="next-head"><meta property="fb:app_id" content="1775481339348651" class="next-head"><meta itemprop="name" content="repl.it" class="next-head"><meta itemprop="description" content="Powerful and simple online compiler, IDE, interpreter, and REPL. Code, compile, and run code in 30+ programming languages: Clojure, Haskell, Kotlin (beta), QBasic, Forth, LOLCODE, BrainF, Emoticon, Bloop, Unlambda, JavaScript, CoffeeScript, Scheme, APL, Lua, Python 2.7, Ruby, Roy, PHP, Python, Nodejs, Enzyme, Go, Java, C++, C++11, C, C#, F#, HTML, CSS, JS, Rust, Swift, Python (with Turtle), Jest, Django, Express, Sinatra, Ruby on Rails, R, Next.js, GatsbyJS, React, React Typescript, React Reason, bash, Quil" class="next-head"><meta name="description" content="Powerful and simple online compiler, IDE, interpreter, and REPL. Code, compile, and run code in 30+ programming languages: Clojure, Haskell, Kotlin (beta), QBasic, Forth, LOLCODE, BrainF, Emoticon, Bloop, Unlambda, JavaScript, CoffeeScript, Scheme, APL, Lua, Python 2.7, Ruby, Roy, PHP, Python, Nodejs, Enzyme, Go, Java, C++, C++11, C, C#, F#, HTML, CSS, JS, Rust, Swift, Python (with Turtle), Jest, Django, Express, Sinatra, Ruby on Rails, R, Next.js, GatsbyJS, React, React Typescript, React Reason, bash, Quil" class="next-head"><meta name="keywords" content="Interpreters,Compilers,Teach,Learn,Code,REPL,Compiler,Clojure,Haskell,Kotlin (beta),QBasic,Forth,LOLCODE,BrainF,Emoticon,Bloop,Unlambda,JavaScript,CoffeeScript,Scheme,APL,Lua,Python 2.7,Ruby,Roy,PHP,Python,Nodejs,Enzyme,Go,Java,C++,C++11,C,C#,F#,HTML, CSS, JS,Rust,Swift,Python (with Turtle),Jest,Django,Express,Sinatra,Ruby on Rails,R,Next.js,GatsbyJS,React,React Typescript,React Reason,bash,Quil" class="next-head"><meta name="author" property="og:author" content="repl.it" class="next-head"><meta name="twitter:card" content="summary" class="next-head"><meta name="twitter:site" content="@replit" class="next-head"><meta name="twitter:description" content="Powerful and simple online compiler, IDE, interpreter, and REPL. Code, compile, and run code in 30+ programming languages: Clojure, Haskell, Kotlin (beta), QBasic, Forth, LOLCODE, BrainF, Emoticon, Bloop, Unlambda, JavaScript, CoffeeScript, Scheme, APL, Lua, Python 2.7, Ruby, Roy, PHP, Python, Nodejs, Enzyme, Go, Java, C++, C++11, C, C#, F#, HTML, CSS, JS, Rust, Swift, Python (with Turtle), Jest, Django, Express, Sinatra, Ruby on Rails, R, Next.js, GatsbyJS, React, React Typescript, React Reason, bash, Quil" class="next-head"><meta name="google" value="notranslate" class="next-head"><link rel="stylesheet" href="./hello_files/vs.min.css" class="next-head"><link rel="stylesheet" type="text/css" href="./hello_files/slick.min.css" class="next-head"><link rel="stylesheet" type="text/css" href="./hello_files/slick-theme.min.css" class="next-head"><link href="./hello_files/css" rel="stylesheet" type="text/css" class="next-head"><link href="./hello_files/saved_resource" rel="stylesheet" type="text/css" class="next-head"><meta name="viewport" content="initial-scale=1.0, width=device-width" class="next-head"><link href="./hello_files/saved_resource" rel="stylesheet" type="text/css" class="next-head"><style>
    * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  min-height: 100%;
}

button {
  border-radius: 0;
}

a {
  color: #4183C4;
  text-decoration: none;
  cursor: pointer;
  border-bottom: 1px solid transparent;
}

a:hover, a:active, a:focus {
  border-bottom: 1px solid #4183C4;
}

header {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;
  height: 60px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  border-bottom: 1px solid #ececec;
}

header .logo {
  position: absolute;
  left: 25px;
  height: 60px;
  line-height: 94px;
}

header .logo img {
  width: 116px;
}

#page {
  height: 100%;
  padding-top: 60px;
  padding-bottom: 433px;
}

@media all and (max-width : 720px) {
  #page {
    padding-bottom: 0;
  }
}

/* Blog */

.postItem {
  width: 720px;
  margin: 50px auto 50px;
}

.post-seperator {
  width: 800px;
  margin-top: 20px;
  margin-left: -40px;
  border-top: 1px solid #ececec;
}

.postItem:last-child .post-seperator {
  display: none;
}

.postItem img {
  display: block;
  margin: 50px auto;
  max-width: 100%;
}

.postItem img + em {
  display: block;
  text-align: center;
  margin-top: -40px;
  font-size: 18px;
}

@media all and (max-width : 800px) {
  .post-seperator {
    width: 100%;
    margin-left: auto;
  }
}

.postTitle a {
  font-size: 40px;
  line-height: 1.15;
  font-family: Raleway;
  font-weight: 100;
  color: #807F7F;
}

.postTitle a:hover {
  color: #4183C4
}

.postAuthor {
  font-family: Lato;
  font-weight: 300;
  font-size: 18px;
  margin-top: 15px;
  color: #807F7F;
}

.postContent {
  font-family: "Miller Text Rom", Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: 18px;
  line-height: 1.6;
  margin-top: 45px;
  color: rgb(93, 91, 91);
}
.postContent h1,
.postContent h2,
.postContent h3,
.postContent h4,
.postContent h5 {
  color: rgb(76, 75, 75);
  font-family: Lato;
  font-weight: 400;
  margin-top: 10px;
}

.postContent h1 {
  font-size: 30px;
  color: rgb(63, 64, 63);
  margin-top: 20px;
}

.postContent h2 {
  font-size: 26px;
  margin-top: 20px;
}

.postContent h3 {
  font-size: 24px;
}

.postContent h4 {
  font-size: 22px;
}

.postContent h5 {
  font-size: 20px;
}

@media all and (max-width : 720px) {
  .postItem {
    width: auto;
    margin: 50px 18px;
  }

  .postContent {
    font-size: 18px
  }

  .postAuthor {
    font-size: 16px;
  }

  .postContent h1 {
    font-size: 28px;
  }

  .postContent h2 {
    font-size: 24px;
  }

  .postContent h3 {
    font-size: 22px;
  }

  .postContent h4 {
    font-size: 20px;
  }

  .postContent h5 {
    font-size: 18px;
  }
}

.postContent p {
  margin-top: 20px;
  margin-bottom: 20px;
}

.postContent ul {
  padding-left: 5px;
}

.postContent ol {
  padding-left: 25px
}

.postContent ul {
  list-style: none;
}

.postContent ul, .postContent ol {
  margin: 20px 0;
}

.postContent ul > li:before {
  content: "• ";
  line-height: 0;
  color: #807F7F;
}

/* Nested */
.postContent ul > li > ul > li:before {
  content: "◦ ";
  line-height: 0;
  color: #807F7F;
}

.postContent ul > li {
  padding-left: 1em;
  text-indent: -.7em;
}

.postContent ol > li {
  text-indent: 0;
}

.postContent li > ul,
.postContent li > ol {
  margin-left: 10px;
}

.postContent pre {
  overflow: auto;
  border: 1px solid #e1e1e8;
  padding: 12px;
  margin-top: 20px  ;
}

.postContent code {
  padding: 2px 4px;
}

.postContent pre code {
  display: block;
  overflow-x: auto;
  color: #000;
  border: none;
}

.postContent code, .postContent pre {
  font-size: 12px;
  line-height: 18px;
  font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;
}

.postContent blockquote {
  font-style: italic;
  border-left: 3px solid black;
  padding-left: 20px;
}

.readMore {
  margin-bottom: 20px;
}

/* Marketing */

.marketingPage {
  font-family: Raleway, sans-serif;
}

.marketingSection {
  text-align: center;
  line-height: 1;
  width: 100%;
  background-color: #fff;
}

.marketingSection:last-child {
  padding-bottom: 100px;
}

.marketingSection h3 {
  font-size: 61px;
  font-weight: 100;
}

.marketingSection > p {
  font-size: 22px;
  margin: 25px auto 0;
  max-width: 700px;
}

.includeTopBorder {
  border-top: 1px solid #ececec;
}

.marketingHeader {
  background-color: #fff;
  color: #807F7F;
  min-height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}

.marketingHeader .button {
  margin-top: 25px;
}

.marketingHeader .scrolldownWrapper {
  width: 40px;
  height: 40px;
  position: absolute;
  bottom: 30px;
  right: 0;
  left: 0;
  margin-right: auto;
  margin-left: auto;
  -webkit-animation-duration: 0.75s;
  animation-duration: 0.75s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

.marketingHeader .scrolldown {
  width: 20px;
  height: 20px;
  border-right: 1px solid #807F7F;
  border-bottom: 1px solid #807F7F;
  transform: rotate(45deg);
  margin: auto;
}

@keyframes fadeInDown {
  0% {
     opacity: 0;
     transform: translateY(-40px);
  }
  100% {
     opacity: 1;
     transform: translateY(0);
  }
}

.fadeInDown {
  -webkit-animation-name: fadeInDown;
  animation-name: fadeInDown;
}

.featuresWrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.marketingFeature {
  margin-top: 50px;
  max-width: 500px;
  text-align: left;
  display: inline-flex;
  line-height: 1.5;
}

.marketingFeature:nth-child(odd) {
  margin-right: 70px;
}

.marketingFeature .img {
  flex: 1;
  height: 100px;
  width: 100px;
  background-size: contain;
  background-repeat: no-repeat;
}

.cloudcode {
  background-image: url('/public/images/cloudcode.png')
}
.languages {
  background-image: url('/public/images/languages2.png')
}
.secure {
  background-image: url('/public/images/lock.png')
}
.console {
  background-image: url('/public/images/console2.png')
}

.marketingFeature .textWrapper {
  flex: 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 20px;
}

.marketingFeature .title {
  font-size: 19px;
  font-weight: 600;
  margin-bottom: 10px;
}

.marketingFeature .details {
  font-size: 17px;
}

.marketingCard {
  display: inline-block;
  vertical-align: top;
  width: 33.33%;
}

.marketingCard .cardImg {
  width: 185px;
  height: 185px;
  margin: auto;
  padding-bottom: 20px;
  background-size: contain;
  background-repeat: no-repeat;
}

.marketingCard h5 {
  color: #807F7F;
  font-size: 18px;
  width: 185px;
  margin: 30px auto 0;
  line-height: 1.5;
}

@media all and (max-width : 720px) {
  .marketingCard {
    display: block;
    width: auto;
  }

  .marketingSection h3 {
    font-size: 50px;
    font-weight: 100;
  }
}

/* Classrooms */

.taheader {
  background-color: #5192b3;
  color: #FFF;
  padding: 0 20px;
}

.taheader .scrolldown {
  border-right: 1px solid #fff;
  border-bottom: 1px solid #fff;
}

.tacontact {
  background-color: #F2F2F3;
  color: #807F7F;
  font-size: 22px;
  margin-bottom: -70px;
  border-bottom: 2px solid rgb(222, 222, 222);
  padding-top: 30px;
}

.tacontact p:first-of-type {
  padding-top: 30px;
  margin-bottom: 50px;
  line-height: 1.5;
}

.tacontact .contactLinkContainer {
  color: #4183C4;
  margin: 20px auto;
  display: block;
}

.tacontact .contactLinkContainer a {
  color: #4183C4;
  text-decoration: none;
  position: relative;
  font-size: 18px;
  margin: 0 30px;
}

.tacontact .twitter, .tacontact .facebook {

}

.aboutContact .twitter, .tacontact .twitter {
  background-image: url('/public/images/twitter.png');
  display: inline-block;
  background-size: contain;
  height: 24px;
  width: 24px;
  background-repeat: no-repeat;
  vertical-align: text-bottom;
}

.aboutContact .facebook, .tacontact .facebook {
  background-image: url('/public/images/facebook.png');
  display: inline-block;
  background-size: contain;
  height: 24px;
  width: 24px;
  background-repeat: no-repeat;
  vertical-align: text-bottom;
}

.taconnect {
  background-color: #FFF;
  color: #807F7F;
  min-height: 600px;
  padding: 50px 0;
}

.taconnect h3 {
  font-size: 40px;
}

.taconnect > p {
  font-size: 22px;
  padding-top: 100px;
}

.tacards {
  margin-top: 110px;
}

.cardImg.student {
  background-image: url('/public/images/student.png');
}

.cardImg.teacher {
  background-image: url('/public/images/teacher.png');
}

.cardImg.progress {
  background-image: url('/public/images/progress.png');
}

.taenvironment {
  color: #807F7F;
  height: 900px;
}

.taenvironment h3 {
  padding-top: 100px;
}

.studentEnvironmentImg {
  background-image: url('/public/images/studentenvironment.png');
  min-height: 500px;
  width: 1250px;
  background-size: cover;
  background-repeat: no-repeat;
  margin: 100px auto 0;
}

@media all and (max-width : 1280px) {
  .studentEnvironmentImg {
    height: 500px;
    width: 100%;
    background-size: contain;
  }
}

.tafeatures {
  color: #807F7F;
  background-color: rgba(242, 242, 242, 1);
  min-height: 500px;
  display: flex;
  align-items: center;
  padding-bottom: 30px;
}

.taschools {
  background-color: #F2F2F3;
  height: 415px;
  padding: 0 15%;
}

.schoolsSlider {
  margin: 0 auto;
}

.taschools > p {
  padding-top: 100px;
  color: #807F7F;
  font-size: 22px;
  margin: 0 auto 100px;
}

.tauser_logo {
  display: inline-block;
  height: 90px;
  width: 100%;
  margin: auto;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.alpha {
  background-image: url('/public/images/classrooms_clients/alpha_ps.png');
}
.columbia_uni_ny {
  background-image: url('/public/images/classrooms_clients/columbia_uni.png');
}
.coast_mountain_academy {
  background-image: url('/public/images/classrooms_clients/coast_mountain_academy.png');
}
.flocabulary {
  background-image: url('/public/images/classrooms_clients/flocabulary.png');
}
.guilsborough {
  background-image: url('/public/images/classrooms_clients/guilsborough.png');
}
.lonestar {
  background-image: url('/public/images/classrooms_clients/lonestar.png');
}
.madeira_city_schools {
  background-image: url('/public/images/classrooms_clients/madeira_city_schools.jpg');
}
.nait {
  background-image: url('/public/images/classrooms_clients/nait.png');
}
.perse {
  background-image: url('/public/images/classrooms_clients/perse.png');
}
.richard_college {
  background-image: url('/public/images/classrooms_clients/richard_college.png');
}
.sfusd {
  background-image: url('/public/images/classrooms_clients/sfusd.png');
}
.uni_of_oregon {
  background-image: url('/public/images/classrooms_clients/uni_of_oregon.png');
}
.utc_oxford {
  background-image: url('/public/images/classrooms_clients/utc_oxford.png');
}
.willington_academy {
  background-image: url('/public/images/classrooms_clients/willington_academy.png');
}
.workshop_college {
  background-image: url('/public/images/classrooms_clients/workshop_college.png');
}
.wyncode {
  background-image: url('/public/images/classrooms_clients/wyncode.png');
}

.tatestimonials {
  padding: 100px 15%;
}

.testimonial {
  margin-bottom: 100px;
  position: relative;
  max-width: 700px;
  margin: 0 auto;
}

.testimonialsSlider {
  width: 90%;
  max-width: 700px;
  margin: 0 auto;
}
.testimonial_auth_pic {
  border-radius: 100px;
  margin-bottom: 32px;
  height: 100px;
  width: 100px;
  margin: 0 auto 32px;
  background-size: contain;
  background-repeat: no-repeat;
}

.testimonial_quote {
  min-height: 90px;
  font-size: 20px;
  margin: 0 auto 42px;
  color: rgb(128, 127, 127);
  line-height: 28px;
  font-style: italic;
}

.quote {
  background-image: url('/public/images/quote.png');
  height: 30px;
  width: 22px;
  display: inline-block;
  background-size: contain;
  background-repeat: no-repeat;
  vertical-align: bottom;
}

.quote:nth-child(even) {
  transform: scaleX(-1);
  height: 18px;
  margin-left: 5px;
  vertical-align: text-bottom;
}

.testimonial_author_info {
  font-size: 20px;
  color: rgb(68, 67, 67);
}

.testimonial_arrow {
  position: absolute;
  top: 150px;
}

.prev.testimonial_arrow {
  left: -45px;
}

.next.testimonial_arrow {
  right: -45px;
}

.nguyen {
  background-image: url('/public/images/nguyen.png');
}

.steve {
  background-image: url('/public/images/steve.jpg');
}

.zach {
  background-image: url('/public/images/zach.jpg');
}

.quincy {
  background-image: url('/public/images/quincy.jpg');
}

#thanks {
  display: none;
}

/* About us */

.aboutHeader h3 {
  color: #F06A60;
}

.aboutHeader p {
  line-height: 1.5;
}

.aboutTeam {
  color: #807F7F;
  border-top: 1px solid #ECECEC;
  min-height: 665px;
}

.aboutTeam > h3 {
  padding-top: 100px;
}

.teamMembers {
  margin-top: 100px;
}

.teamMembers .marketingCard {
  width: 16%;
}

@media all and (max-width : 720px) {
  .teamMembers .marketingCard {
    display: block;
    margin: 0 auto;
    margin-bottom: 30px;
    width: auto;
  }
}

.memberImg {
  border-radius: 100%;
}

.faris {
  background-image: url('/public/images/faris.jpg');
}
.amjad {
  background-image: url('/public/images/amjad.jpg');
}
.haya {
  background-image: url('/public/images/haya.jpg?x=1');
  position: relative;
  right: 10px;
}
.mason {
  background-image: url('/public/images/mason.png?x=1');
}
.tim {
  background-image: url('/public/images/tim.png');
}
.rob {
  background-image: url('/public/images/rob.png');
}

.memberName {
  font-size: 40px;
  font-weight: 100;
  margin-top: 20px;
}

.memberDescription {
  width: 100% !important;
  margin-top: 10px !important;
}

.memberTwitter {
  font-weight: normal;
}

.aboutContact {
  background-color: #F2F2F3;
  color: #807F7F;
  height: 400px;
}

.aboutContact h3 {
  padding-top: 100px;
  margin-bottom: 20px;
}

.aboutContact a {
  display: inline-block;
  margin-top: 25px;
  font-size: 18px;
}

@media all and (max-width : 720px) {
  .marketingSection.jobsSection .content {
    width: auto;
    margin: 50px 18px;
  }

  .jobsSection .content h3 {
    font-size: 22px;
  }

  .jobsSection .content p {
    font-size: 18px;
  }
}

/* Feedback */
.feedbackIframe {
  border: 0;
  box-sizing: border-box;
  max-height: 100%;
  border-left: 1px solid silver;
  border-right: 1px solid silver;
}

@media all and (max-width : 480px) {
  .feedbackIframe {
    margin-top: 20px;
    border: 0;
  }
}

/* Bot */

.slack-add {
  margin-right: 20px;
  display: inline-block;
  height: 40px;
  border: none;
}

.slack-add img {
  height: 40px;
  width: 140px;
  margin: 0;
  max-width: none;
}

.fb-msg {
  cursor:pointer;
  text-decoration:none;
  border: none;
}

.slack-add:hover, .fb-msg:hover {
  border: none;
  opacity: 0.8;
}

.fb-msg span {
  height: 40px;
  width: 139px;
  line-height: 40px;
  text-align: center;
  border-radius: 4px;
  background: #0084ff;
  color: #fff;
  font-size: 14px;
  display:inline-block;
  font-family: helvetica, arial, sans-serif;
  white-space: nowrap;
}

#landing-language-cycle{
  display: inline-block;
  text-align: left;
  width: 100px;
  white-space: nowrap;
}

.teacher-start-nav {
  background: #F7F8F9;
  color: #797B7C;
  padding: 0 1em;
}

.teacher-start-nav:hover {
  background: rgb(81, 146, 179);
  color: #fff;
}

.mainLandingHeader {
  padding: 1em 4em 2em 2em;
  font-size: 22px;
  min-height: calc(83vh - 60px);
}

.mainLandingHeader .teachers-start {
  height: 55px;
  width: 380px;
  max-width: calc(100% - 40px);
  font-weight: 400;
  font-size: 19px;
  font-family: 'Questrial';
  padding: 0;
  border: none;

  background: #F7F8F9;
  color: #797B7C;
}

.mainLandingHeader .teachers-start:hover {
  background: rgb(81, 146, 179);
  color: #FFF;
}

.mainLandingHeader .bot-container {
  position: relative;
  width: 380px;
  max-width: calc(100% - 40px);
  height: 35px;
  z-index: 2;
}

.mainLandingHeader .bot {
  position: absolute;
  bottom: -36px;
  right: 4px;
  width: 70px;
}

.mainLandingHeader .language-search-placeholder {
  background: #fff;
  min-height: 55px;
  width: 380px;
  line-height: 55px;
  border: 1px solid #4083C4;
  color: #000;
  font-size: 19px;
  padding-left: 12px;
  outline: none;
}

.mainLandingHeader .heading {
  margin-bottom: .75em;
  color: #2E4457;
}

.mainLandingHeader .heading.roles {
  font-style: italic;
}

.mainLandingHeader h2 {
  font-weight: 500;
}

.mainLandingHeader h4 {
  font-weight: 300;
  font-size: 1.25em;
}

.mainLandingHeader .title-em {
  font-weight: 800;
  font-style: normal;
}

.mainLandingFeatures,
.mainLandingClassroom {
  padding-top: 100px;
  padding-bottom: 100px;
}

.mainLandingFeatures p {
  margin-bottom: 50px;
}

.mainLandingClassroom {
  background: rgba(170,218,245,0.17);
}

.mainLandingClassroom h3 {
  color: rgb(81, 146, 179);
}

.mainLandingClassroom p,
.mainLandingClassroom p a {
  color: #807F7F;
  font-size: 22px;
  text-decoration: none;
}

.mainLandingClassroom .moreInfo {
  font-size: 16px;
}

.mainLandingClassroom .moreInfo:hover {
  border-bottom: 0;
  color: rgb(81, 146, 179);
}

.mainLandingClassroom p a:hover {
  border-bottom: 1px solid #807F7F;
}

.mainLandingClassroom .button {
  margin-top: 50px;
}

.mainLandingFeatures {
  color: #807F7F;
}

.mainLandingBlog {
  border-top: 1px solid #ececec;
}

.mainLandingBlog .subtitle {
  font-size: 22px;
  margin: 0 auto 50px;
  max-width: 700px;
  color: #807F7F;
  text-align: center;
  line-height: 1;
  width: 100%;
  background-color: #fff;
}

@media all and (min-width: 880px) {
  .mainLandingBlog .postItem {
    margin: 0;
    margin-left: 150px;
  }
}

.zero {
  font-size: 25px;
}

.introVideo {
  max-width: 820px;
  display: block;
  margin: 100px auto 100px;
  height: 100%;
  position: relative;
  background: black;
}

.taconnect .introVideo {
  margin: 20px auto 50px;
}

.introVideo .thumbnailWrapper {
  cursor: pointer;
}

.introVideo iframe,
.introVideo .thumb {
  max-width: 100%;
  width: 100%;
  display: block;
  height: 461px;
  border: none;
  top: 0;
  bottom: 0;
  margin: auto 0;
}

.introVideo .thumb {
  max-height: 461px;
  width: auto;
  height: auto;
}

.introVideo .play {
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  display: inline-block;
  background-size: contain;
  height: 80px;
  width: 80px;
  background-repeat: no-repeat;
  background-image: url('/public/images/youtube-play.png');
}

.introVideo .thumbnailWrapper:hover .play{
  background-image: url('/public/images/youtube-play-hover.png');
}

@media all and (max-width: 830px) {
  .introVideo {
    max-width: 90%;
  }
}

@media all and (max-width: 600px) {
  .introVideo iframe {
    height: 320px;
  }

  .introVideo .thumb {
    max-height: 320px
  }

  .introVideo .play {
    height: 45px;
    width: 64px;
  }
}

@media all and (max-width: 480px) {
  .introVideo iframe {
    height: 230px;
  }

  .introVideo .thumb {
    max-height: 230px
  }

  .introVideo .play {
    height: 36px;
    width: 51px;
  }
}

@keyframes loader-fill-animation {
    0% { width: 0%; }
    90% { width: 100%; }
}

@keyframes loading-spinner {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.loading-spinner {
  width: 64px;
  height: 64px;

  background-image: url('/public/images/logo.svg');
  background-position: center;
  background-size: contain;

  transform: rotate(0deg);

  animation-name: loading-spinner;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}

.css-typer-character {
  animation-duration: 0.01s;
  animation-name: css-typer-show;
  animation-fill-mode: both;
}

@keyframes css-typer-show {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.page-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background-image: url(/public/images/close.png);
  height: 15px;
  width: 15px;
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  cursor: pointer;
}

.page-close:hover {
  background-image: url(/public/images/close_hover.png);
}
</style><script type="text/javascript" async="" src="./hello_files/recaptcha__en.js.download"></script><script type="text/javascript" async="" src="./hello_files/analytics.min.js.download"></script><script async="" src="./hello_files/analytics.js.download"></script><script src="./hello_files/polyfill.min.js.download" class="next-head"></script><script class="next-head">
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-25629695-1', 'auto');
    ga('send', 'pageview');</script><script class="next-head">
    !function(){
      var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="4.0.0";
    analytics.load('jdVID8rHoI7wkCBDjKmjApGBGWclWIKJ');
    analytics.page();
    }}();</script><script class="next-head">
    (function (isTouchDevice) {
      if (!isTouchDevice) return;
      var isTouchClass = 'is-touch-device';
      var docElement = document.documentElement;
      docElement.className = docElement.className ? [docElement.className, isTouchClass].join(' ') : isTouchClass;
    })(('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch);
            </script><link rel="preload" href="./hello_files/index.js.download" as="script"><link rel="preload" href="./hello_files/_app.js.download" as="script"><link rel="preload" href="./hello_files/_error.js.download" as="script"><link rel="preload" href="./hello_files/main-000e04511466974b7b0d.js.download" as="script"><style id="__jsx-3633663456">.email-verification-banner.jsx-3633663456{font-family:Questrial;border-color:#E2A8A7;border-style:solid;border-width:1px 0px;color:#D56D6D;background-color:#FEF1F1;width:100%;text-align:center;padding:10px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}
.email-verification-banner.jsx-3633663456 a.jsx-3633663456{color:#4183C4;}
.email-verification-banner.jsx-3633663456 a.jsx-3633663456:hover{border-bottom:1px solid #4183C4;cursor:pointer;}</style><style id="__jsx-3485800696">#nprogress{pointer-events:none;}
.nprogress-bar{background:#4183C4;position:fixed;z-index:400001;top:0;left:0;width:100%;height:2px;}
.nprogress-static-css-bar{width:0;-webkit-animation:10s ease-out 750ms 1 normal both running nprogress-widen;animation:10s ease-out 750ms 1 normal both running nprogress-widen;}
@-webkit-keyframes nprogress-widen{0%{width:0;}100%{width:90%;}}
@keyframes nprogress-widen{0%{width:0;}100%{width:90%;}}
.nprogress-peg{display:block;position:absolute;right:0px;width:100px;height:100%;box-shadow:0 0 10px #4183C4,0 0 5px #4183C4;opacity:1.0;-webkit-transform:rotate(3deg) translate(0px,-4px);-ms-transform:rotate(3deg) translate(0px,-4px);-webkit-transform:rotate(3deg) translate(0px,-4px);-ms-transform:rotate(3deg) translate(0px,-4px);transform:rotate(3deg) translate(0px,-4px);}
.nprogress-spinner{display:block;position:fixed;z-index:1031;top:15px;right:15px;}
.nprogress-spinner-icon{width:18px;height:18px;box-sizing:border-box;visibility:hidden;border:solid 2px transparent;border-top-color:#29d;border-left-color:#29d;border-radius:50%;-webkit-animation:nprogress-spinner 400ms linear infinite;-webkit-animation:nprogress-spinner 400ms linear infinite;animation:nprogress-spinner 400ms linear infinite;-webkit-animation-delay:11s;animation-delay:11s;}
@-webkit-keyframes nprogress-spinner{0%{-webkit-transform:rotate(0deg);visibility:visible;}100%{-webkit-transform:rotate(360deg);}}
@-webkit-keyframes nprogress-spinner{0%{-webkit-transform:rotate(0deg);visibility:visible;}100%{-webkit-transform:rotate(360deg);-ms-transform:rotate(360deg);transform:rotate(360deg);}}
@keyframes nprogress-spinner{0%{-webkit-transform:rotate(0deg);visibility:visible;}100%{-webkit-transform:rotate(360deg);-ms-transform:rotate(360deg);transform:rotate(360deg);}}</style><script type="text/javascript">KNOWN_LANGUAGES = JSON.parse(atob('eyJjbG9qdXJlIjp7ImRpc3BsYXlOYW1lIjoiQ2xvanVyZSIsInRhZ2xpbmUiOiJBIG1vZGVybiBKVk0tYmFzZWQgTGlzcCBkaWFsZWN0IHdpdGggYSBmb2N1cyBvbiBpbW11dGFiaWxpdHkiLCJrZXkiOiJjbG9qdXJlIiwiZW50cnlwb2ludCI6Im1haW4uY2xqIiwiZXh0IjoiY2xqIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6IkNsb2p1cmUgMS44LjBcbkphdmEgSG90U3BvdChUTSkgNjQtQml0IFNlcnZlciBWTSAxLjguMF85MS1iMTQiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY2xvanVyZS5zdmciLCJ0ZW1wbGF0ZSI6IiIsIm1hdGNoaW5ncyI6W10sImVuZ2luZSI6ImdvdmFsIn0sImhhc2tlbGwiOnsiZGlzcGxheU5hbWUiOiJIYXNrZWxsIiwidGFnbGluZSI6IkFuIGFkdmFuY2VkLCBwdXJlbHkgZnVuY3Rpb25hbCBwcm9ncmFtbWluZyBsYW5ndWFnZSIsImtleSI6Imhhc2tlbGwiLCJlbnRyeXBvaW50IjoibWFpbi5ocyIsImV4dCI6ImhzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6IkdIQ2ksIHZlcnNpb24gOC4wLjEiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvaGFza2VsbC5zdmciLCJ0ZW1wbGF0ZSI6IiIsIm1hdGNoaW5ncyI6W10sImVuZ2luZSI6ImdvdmFsIn0sImtvdGxpbiI6eyJkaXNwbGF5TmFtZSI6IktvdGxpbiAoYmV0YSkiLCJ0YWdsaW5lIjoiU3RhdGljYWxseSB0eXBlZCBwcm9ncmFtbWluZyBsYW5ndWFnZSBpbnRlcm9wZXJhYmxlIHdpdGggSmF2YSBhbmQgQW5kcm9pZCIsImtleSI6ImtvdGxpbiIsImVudHJ5cG9pbnQiOiJtYWluLmt0IiwiZXh0Ijoia3QiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6IldlbGNvbWUgdG8gS290bGluIHZlcnNpb24gMS4wLjMiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMva290bGluLnN2ZyIsInRlbXBsYXRlIjoiIiwibWF0Y2hpbmdzIjpbXSwiZW5naW5lIjoiZ292YWwifSwicWJhc2ljIjp7ImRpc3BsYXlOYW1lIjoiUUJhc2ljIiwiZW5naW5lIjoicmVwbGJveCIsInRhZ2xpbmUiOiJTdHJ1Y3R1cmVkIHByb2dyYW1taW5nIGZvciBiZWdpbm5lcnMuIiwiaGVhZGVyIjoiUUJhc2ljIChxYi5qcylcbkNvcHlyaWdodCAoYykgMjAxMCBTdGV2ZSBIYW5vdiIsImNhdGVnb3J5IjoiQ2xhc3NpYyIsImV4dCI6ImJhcyIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwia2V5IjoicWJhc2ljIn0sImZvcnRoIjp7ImRpc3BsYXlOYW1lIjoiRm9ydGgiLCJlbmdpbmUiOiJyZXBsYm94IiwidGFnbGluZSI6IkFuIGludGVyYWN0aXZlIHN0YWNrLW9yaWVudGVkIGxhbmd1YWdlLiIsImhlYWRlciI6IkpTLUZvcnRoIDAuNTIwMDgwNDE3MTM0MlxuaHR0cDovL3d3dy5mb3J0aGZyZWFrLm5ldC9qc2ZvcnRoLmh0bWxcblRoaXMgcHJvZ3JhbSBpcyBwdWJsaXNoZWQgdW5kZXIgdGhlIEdQTC4iLCJjYXRlZ29yeSI6IkNsYXNzaWMiLCJleHQiOiJmdGgiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImtleSI6ImZvcnRoIn0sImxvbGNvZGUiOnsiZGlzcGxheU5hbWUiOiJMT0xDT0RFIiwiZW5naW5lIjoicmVwbGJveCIsInRhZ2xpbmUiOiJUaGUgYmFzaWMgbGFuZ3VhZ2Ugb2YgbG9sY2F0cy4iLCJoZWFkZXIiOiJMT0xDT0RFIHYxLjIgKGxvbC1jb2ZmZWUpXG5Db3B5cmlnaHQgKGMpIDIwMTEgTWF4IFNoYXdhYmtlaCIsImNhdGVnb3J5IjoiRXNvdGVyaWMiLCJleHQiOiJsb2wiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xvbGNvZGUuc3ZnIiwia2V5IjoibG9sY29kZSJ9LCJicmFpbmZ1Y2siOnsiZGlzcGxheU5hbWUiOiJCcmFpbkYiLCJlbmdpbmUiOiJyZXBsYm94IiwidGFnbGluZSI6IkEgcHVyZSBUdXJpbmcgbWFjaGluZSBjb250cm9sbGVyLiIsImhlYWRlciI6IkJyYWluRioqKiwgYmZqc1xuQ29weXJpZ2h0IChjKSAyMDExIEFtamFkIE1hc2FkIiwiY2F0ZWdvcnkiOiJFc290ZXJpYyIsImV4dCI6ImJmIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9icmFpbmZ1Y2suc3ZnIiwia2V5IjoiYnJhaW5mdWNrIn0sImVtb3RpY29uIjp7ImRpc3BsYXlOYW1lIjoiRW1vdGljb24iLCJlbmdpbmUiOiJyZXBsYm94IiwidGFnbGluZSI6IlByb2dyYW1taW5nIHdpdGggYW4gZXh0cmEgZG9zZSBvZiBzbWlsZS4iLCJoZWFkZXIiOiJFbW90aWNvbiB2MS41IChlbW90aWNvZmZlZSlcbkNvcHlyaWdodCAoYykgMjAxMSBBbWphZCBNYXNhZCIsImNhdGVnb3J5IjoiRXNvdGVyaWMiLCJleHQiOiJlbW90aWNvbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwia2V5IjoiZW1vdGljb24ifSwiYmxvb3AiOnsiZGlzcGxheU5hbWUiOiJCbG9vcCIsImVuZ2luZSI6InJlcGxib3giLCJ0YWdsaW5lIjoiTm90aGluZyBidXQgYm91bmRlZCBsb29wcy4iLCJoZWFkZXIiOiJCbG9vUGpzXG5Db3B5cmlnaHQgKGMpIDIwMDUgVGltIENhbWVyb24gUnlhblxuQmFzZWQgb24gUGVybCBjb2RlIGJ5IEpvaG4gQ293YW4sIDE5OTQiLCJjYXRlZ29yeSI6IkVzb3RlcmljIiwiZXh0IjoiYmxvb3AiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImtleSI6ImJsb29wIn0sInJlYWN0X25hdGl2ZSI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IE5hdGl2ZSIsInRhZ2xpbmUiOiJDcmVhdGUgbW9iaWxlIGFwcHMgd2l0aCBSZWFjdCBOYXRpdmUgYW5kIEV4cG8iLCJrZXkiOiJyZWFjdF9uYXRpdmUiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJSZWFjdCBOYXRpdmUiLCJjYXRlZ29yeSI6IlBvcHVsYXIiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsInRlbXBsYXRlIjoiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IEJ1dHRvbiwgVmlldyB9IGZyb20gJ3JlYWN0LW5hdGl2ZSc7XG5cbmNvbnN0IHByZXNzQ291bnQgPSAwO1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBBcHAgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQge1xuICBjb25zdHJ1Y3Rvcihwcm9wcykge1xuICAgIHN1cGVyKHByb3BzKVxuXG4gICAgdGhpcy5zdGF0ZSA9IHtcbiAgICAgIHByZXNzQ291bnQ6IDAsXG4gICAgfVxuICB9XG5cbiAgY29tcG9uZW50RGlkVXBkYXRlKCkge1xuICAgIGNvbnNvbGUubG9nKCdQcmVzcyBDb3VudDogJywgdGhpcy5zdGF0ZS5wcmVzc0NvdW50KTtcbiAgfVxuXG4gIHJlbmRlcigpIHtcbiAgICByZXR1cm4gKFxuICAgICAgPFZpZXcgc3R5bGU9e3twb3NpdGlvbjogJ3JlbGF0aXZlJywgdG9wOiAxMDB9fT5cbiAgICAgICAgPEJ1dHRvblxuICAgICAgICAgIHRpdGxlPVwiUHJlc3MgTWUhXCJcbiAgICAgICAgICBvblByZXNzPXsoKSA9PiB0aGlzLnNldFN0YXRlKHtwcmVzc0NvdW50OiB0aGlzLnN0YXRlLnByZXNzQ291bnQgKyAxfSl9XG4gICAgICAgIC8+XG4gICAgICA8L1ZpZXc+XG4gICAgKVxuICB9XG59IiwibWF0Y2hpbmdzIjpbXSwiZW5naW5lIjoiZ292YWwifSwidW5sYW1iZGEiOnsiZGlzcGxheU5hbWUiOiJVbmxhbWJkYSIsImVuZ2luZSI6InJlcGxib3giLCJ0YWdsaW5lIjoiRnVuY3Rpb25hbCBwdXJpdHkgZ2l2ZW4gZm9ybS4iLCJoZWFkZXIiOiJVbmxhbWJkYSB2Mi4wICh1bmxhbWJkYS1jb2ZmZWUpXG5Db3B5cmlnaHQgKGMpIDIwMTEgTWF4IFNoYXdhYmtlaCIsImNhdGVnb3J5IjoiRXNvdGVyaWMiLCJleHQiOiJ1bmwiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImtleSI6InVubGFtYmRhIn0sImphdmFzY3JpcHQiOnsiZGlzcGxheU5hbWUiOiJKYXZhU2NyaXB0IiwiZW5naW5lIjoicmVwbGJveCIsInRhZ2xpbmUiOiJUaGUgZGUgZmFjdG8gbGFuZ3VhZ2Ugb2YgdGhlIFdlYi4iLCJjYXRlZ29yeSI6IldlYiIsImhlYWRlciI6Ik5hdGl2ZSBCcm93c2VyIEphdmFTY3JpcHQiLCJleHQiOiJqcyIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YXNjcmlwdC5zdmciLCJrZXkiOiJqYXZhc2NyaXB0In0sImJhYmVsIjp7ImRpc3BsYXlOYW1lIjoiRVM2IiwiZW5naW5lIjoicmVwbGJveCIsInRhZ2xpbmUiOiJOZXh0IGdlbmVyYXRpb24gSmF2YVNjcmlwdC4iLCJoZWFkZXIiOiJCYWJlbCBDb21waWxlciB2Ni40LjRcbkNvcHlyaWdodCAoYykgMjAxNC0yMDE1IFNlYmFzdGlhbiBNY0tlbnppZSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiZXh0IjoianMiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmFzY3JpcHQuc3ZnIiwia2V5IjoiYmFiZWwifSwiY29mZmVlc2NyaXB0Ijp7ImRpc3BsYXlOYW1lIjoiQ29mZmVlU2NyaXB0IiwiZW5naW5lIjoicmVwbGJveCIsInRhZ2xpbmUiOiJVbmZhbmN5IEphdmFTY3JpcHQuIiwiaGVhZGVyIjoiQ29mZmVlU2NyaXB0IHYxLjEwXG5Db3B5cmlnaHQgKGMpIDIwMTYsIEplcmVteSBBc2hrZW5hcyIsImNhdGVnb3J5IjoiV2ViIiwiZXh0IjoiY29mZmVlIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9jb2ZmZWVzY3JpcHQuc3ZnIiwia2V5IjoiY29mZmVlc2NyaXB0In0sInNjaGVtZSI6eyJkaXNwbGF5TmFtZSI6IlNjaGVtZSIsImVuZ2luZSI6InJlcGxib3giLCJ0YWdsaW5lIjoiQW4gZWxlZ2FudCBkeW5hbWljIGRpYWxlY3Qgb2YgTGlzcC4iLCJoZWFkZXIiOiJCaXdhU2NoZW1lIEludGVycHJldGVyIHZlcnNpb24gMC42LjRcbkNvcHlyaWdodCAoQykgMjAwNy0yMDE0IFl1dGFrYSBIQVJBIGFuZCB0aGUgQml3YVNjaGVtZSB0ZWFtIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJleHQiOiJzYyIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvc2NoZW1lLnN2ZyIsImtleSI6InNjaGVtZSJ9LCJhcGwiOnsiZGlzcGxheU5hbWUiOiJBUEwiLCJlbmdpbmUiOiJyZXBsYm94IiwidGFnbGluZSI6IkFuIGFycmF5LW9yaWVudGVkIGxhbmd1YWdlIHVzaW5nIGZ1bm55IGNoYXJhY3RlcnMuIiwiaGVhZGVyIjoibmduL2FwbCIsImNhdGVnb3J5IjoiQ2xhc3NpYyIsImV4dCI6ImFwbCIsImtleSI6ImFwbCJ9LCJsdWEiOnsiZGlzcGxheU5hbWUiOiJMdWEiLCJ0YWdsaW5lIjoiQSBsaWdodHdlaWdodCBtdWx0aS1wYXJhZGlnbSBzY3JpcHRpbmcgbGFuZ3VhZ2UuIiwia2V5IjoibHVhIiwiZW50cnlwb2ludCI6Im1haW4ubHVhIiwiZXh0IjoibHVhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6Ikx1YSA1LjEgIENvcHlyaWdodCAoQykgMTk5NC0yMDA2IEx1YS5vcmcsIFBVQy1SaW9cbltHQ0MgNC4yLjEgKExMVk0sIEVtc2NyaXB0ZW4gMS41KV0gb24gbGludXgyIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2x1YS5zdmciLCJ0ZW1wbGF0ZSI6IiIsIm1hdGNoaW5ncyI6W10sImVuZ2luZSI6ImdvdmFsIn0sInB5dGhvbiI6eyJkaXNwbGF5TmFtZSI6IlB5dGhvbiIsInRhZ2xpbmUiOiJBIGR5bmFtaWMgbGFuZ3VhZ2UgZW1waGFzaXppbmcgcmVhZGFiaWxpdHkuIiwia2V5IjoicHl0aG9uIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhlYWRlciI6IlB5dGhvbiAyLjcuMTAgKGRlZmF1bHQsIEp1bCAxNCAyMDE1LCAxOTo0NjoyNylcbltHQ0MgNC44LjJdIG9uIGxpbnV4IiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3B5dGhvbi5zdmciLCJ0ZW1wbGF0ZSI6IiIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwifSwicnVieSI6eyJkaXNwbGF5TmFtZSI6IlJ1YnkiLCJ0YWdsaW5lIjoiQSBuYXR1cmFsIGR5bmFtaWMgb2JqZWN0LW9yaWVudGVkIGxhbmd1YWdlLiIsImtleSI6InJ1YnkiLCJlbnRyeXBvaW50IjoibWFpbi5yYiIsImV4dCI6InJiIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGVhZGVyIjoicnVieSAyLjUuMHAwICgyMDE3LTEyLTI1IHJldmlzaW9uIDYxNDY4KSBbeDg2XzY0LWxpbnV4XSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ydWJ5LnN2ZyIsInRlbXBsYXRlIjoiIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJyb3kiOnsiZGlzcGxheU5hbWUiOiJSb3kiLCJlbmdpbmUiOiJyZXBsYm94IiwidGFnbGluZSI6IlNtYWxsIGZ1bmN0aW9uYWwgbGFuZ3VhZ2UgdGhhdCBjb21waWxlcyB0byBKYXZhU2NyaXB0LiIsImhlYWRlciI6IlJveSAwLjEuM1xuQ29weXJpZ2h0IChDKSAyMDExIEJyaWFuIE1jS2VubmEiLCJjYXRlZ29yeSI6IldlYiIsImV4dCI6InJveSIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcm95LnN2ZyIsImtleSI6InJveSJ9LCJwaHAiOnsiZGlzcGxheU5hbWUiOiJQSFAiLCJ0YWdsaW5lIjoiQSBwb3B1bGFyIGdlbmVyYWwtcHVycG9zZSBzY3JpcHRpbmcgbGFuZ3VhZ2UuIiwia2V5IjoicGhwIiwiZW50cnlwb2ludCI6Im1haW4ucGhwIiwiZXh0IjoicGhwIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJQSFAgNy4wLjggKGNsaSkgKGJ1aWx0OiBKdW4gMjMgMjAxNiAyMzozOToxNCkgKCBOVFMgKVxuQ29weXJpZ2h0IChjKSAxOTk3LTIwMTYgVGhlIFBIUCBHcm91cFxuWmVuZCBFbmdpbmUgdjMuMC4wLCBDb3B5cmlnaHQgKGMpIDE5OTgtMjAxNiBaZW5kIFRlY2hub2xvZ2llcyIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9waHAuc3ZnIiwidGVtcGxhdGUiOiIiLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIn0sInB5dGhvbjMiOnsiZGlzcGxheU5hbWUiOiJQeXRob24zIiwidGFnbGluZSI6IkEgZHluYW1pYyBsYW5ndWFnZSBlbXBoYXNpemluZyByZWFkYWJpbGl0eS4iLCJrZXkiOiJweXRob24zIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOnRydWUsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGVhZGVyIjoiUHl0aG9uIDMuNi4xIChkZWZhdWx0LCBEZWMgMjAxNSwgMTM6MDU6MTEpXG5bR0NDIDQuOC4yXSBvbiBsaW51eCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwidGVtcGxhdGUiOiIiLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIn0sIm5vZGVqcyI6eyJkaXNwbGF5TmFtZSI6Ik5vZGVqcyIsInRhZ2xpbmUiOiJFdmVudGVkIEkvTyBmb3IgdjggSmF2YXNjcmlwdC4iLCJrZXkiOiJub2RlanMiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwidGVtcGxhdGUiOiIiLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIn0sImVuenltZSI6eyJkaXNwbGF5TmFtZSI6IkVuenltZSIsInRhZ2xpbmUiOiJBIEphdmFTY3JpcHQgVGVzdGluZyB1dGlsaXR5IGZvciBSZWFjdCIsImtleSI6ImVuenltZSIsImVudHJ5cG9pbnQiOiJpbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHY3LjQgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IlRlc3RpbmciLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsInRlbXBsYXRlIjoiaW1wb3J0IHsgc2hhbGxvdywgbW91bnQgfSBmcm9tICdlbnp5bWUnO1xuXG5mdW5jdGlvbiBDb21wb25lbnQoKSB7IHJldHVybiA8ZGl2IC8+OyB9XG5cbmNvbnN0IHdyYXBwZXIgPSBzaGFsbG93KDxDb21wb25lbnQgLz4pO1xuXG5hc3NlcnQod3JhcHBlci5maW5kKCdkaXYnKS5sZW5ndGggPT09IDEpIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJnbyI6eyJkaXNwbGF5TmFtZSI6IkdvIiwidGFnbGluZSI6IlN0YXRpY2FsbHkgdHlwZWQgeWV0IGV4cHJlc3NpdmUgbGFuZ3VhZ2Ugd2l0aCBhIGZvY3VzIG9uIGNvbmN1cnJlbmN5LiIsImtleSI6ImdvIiwiZW50cnlwb2ludCI6Im1haW4uZ28iLCJleHQiOiJnbyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhlYWRlciI6ImdvIHZlcnNpb24gZ28xLjkuNCBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9nby5zdmciLCJ0ZW1wbGF0ZSI6InBhY2thZ2UgbWFpblxuXG5pbXBvcnQgXCJmbXRcIlxuXG5mdW5jIG1haW4oKSB7XG4gIGZtdC5QcmludGxuKFwiSGVsbG8gV29ybGRcIilcbn0iLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIn0sImphdmEiOnsiZGlzcGxheU5hbWUiOiJKYXZhIiwidGFnbGluZSI6IkEgY29uY3VycmVudCwgY2xhc3MtYmFzZWQsIHN0YXRpY2FsbHkgdHlwZWQgb2JqZWN0LW9yaWVudGVkIGxhbmd1YWdlLiIsImtleSI6ImphdmEiLCJlbnRyeXBvaW50IjoiTWFpbi5qYXZhIiwiZXh0IjoiamF2YSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhlYWRlciI6ImphdmEgdmVyc2lvbiBcIjEuOC4wXzMxXCJcbkphdmEoVE0pIFNFIFJ1bnRpbWUgRW52aXJvbm1lbnQgKGJ1aWxkIDEuOC4wXzMxLWIxMylcbkphdmEgSG90U3BvdChUTSkgNjQtQml0IFNlcnZlciBWTSAoYnVpbGQgMjUuMzEtYjA3LCBtaXhlZCBtb2RlKSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9qYXZhLnN2ZyIsInRlbXBsYXRlIjoiY2xhc3MgTWFpbiB7XG4gIHB1YmxpYyBzdGF0aWMgdm9pZCBtYWluKFN0cmluZ1tdIGFyZ3MpIHtcbiAgICBTeXN0ZW0ub3V0LnByaW50bG4oXCJIZWxsbyB3b3JsZCFcIik7XG4gIH1cbn0iLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIn0sImNwcCI6eyJkaXNwbGF5TmFtZSI6IkMrKyIsInRhZ2xpbmUiOiJBIGdlbmVyYWwgcHVycG9zZSBzeXN0ZW0gcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoiY3BwIiwiZW50cnlwb2ludCI6Im1haW4uY3BwIiwiZXh0IjoiY3BwIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGVhZGVyIjoiZ2NjIHZlcnNpb24gNC42LjMiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY3BwLnN2ZyIsInRlbXBsYXRlIjoiI2luY2x1ZGUgPGlvc3RyZWFtPlxuXG5pbnQgbWFpbigpIHtcbiAgc3RkOjpjb3V0IDw8IFwiSGVsbG8gV29ybGQhXFxuXCI7XG59IiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJjcHAxMSI6eyJkaXNwbGF5TmFtZSI6IkMrKzExIiwidGFnbGluZSI6IkEgZ2VuZXJhbCBwdXJwb3NlIHN5c3RlbSBwcm9ncmFtbWluZyBsYW5ndWFnZS4iLCJrZXkiOiJjcHAxMSIsImVudHJ5cG9pbnQiOiJtYWluLmNwcCIsImV4dCI6ImNwcCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhlYWRlciI6ImdjYyB2ZXJzaW9uIDQuNi4zIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2NwcC5zdmciLCJ0ZW1wbGF0ZSI6IiNpbmNsdWRlIDxpb3N0cmVhbT5cblxuaW50IG1haW4oKSB7XG4gIHN0ZDo6Y291dCA8PCBcIkhlbGxvIFdvcmxkIVxcblwiO1xufSIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwifSwiYyI6eyJkaXNwbGF5TmFtZSI6IkMiLCJ0YWdsaW5lIjoiTG93LWxldmVsIGFuZCBjcm9zcy1wbGF0Zm9ybSBpbXBlcmF0aXZlIGxhbmd1YWdlLiIsImtleSI6ImMiLCJlbnRyeXBvaW50IjoibWFpbi5jIiwiZXh0IjoiYyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhlYWRlciI6ImdjYyB2ZXJzaW9uIDQuNi4zIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2Muc3ZnIiwidGVtcGxhdGUiOiIjaW5jbHVkZSA8c3RkaW8uaD5cblxuaW50IG1haW4odm9pZCkge1xuICBwcmludGYoXCJIZWxsbyBXb3JsZFxcblwiKTtcbiAgcmV0dXJuIDA7XG59IiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJjc2hhcnAiOnsiZGlzcGxheU5hbWUiOiJDIyIsInRhZ2xpbmUiOiJBIE1pY3Jvc29mdCAuTkVUIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6ImNzaGFycCIsImVudHJ5cG9pbnQiOiJtYWluLmNzIiwiZXh0IjoiY3MiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6Ik1vbm8gQyMgY29tcGlsZXIgdmVyc2lvbiA0LjAuNC4wIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2NzaGFycC5zdmciLCJ0ZW1wbGF0ZSI6InVzaW5nIFN5c3RlbTtcblxuY2xhc3MgTWFpbkNsYXNzIHtcbiAgcHVibGljIHN0YXRpYyB2b2lkIE1haW4gKHN0cmluZ1tdIGFyZ3MpIHtcbiAgICBDb25zb2xlLldyaXRlTGluZSAoXCJIZWxsbyBXb3JsZFwiKTtcbiAgfVxufSIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwifSwiZnNoYXJwIjp7ImRpc3BsYXlOYW1lIjoiRiMiLCJ0YWdsaW5lIjoiQSBNaWNyb3NvZnQgLk5FVCBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6ImZzaGFycCIsImVudHJ5cG9pbnQiOiJtYWluLmZzIiwiZXh0IjoiZnMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6IlwiRiMgQ29tcGlsZXIgZm9yIEYjIDQuMCAoT3BlbiBTb3VyY2UgRWRpdGlvbikiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvZnNoYXJwLnN2ZyIsInRlbXBsYXRlIjoiIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJ3ZWJfcHJvamVjdCI6eyJlbmdpbmUiOiJyZXBsYm94IiwiZGlzcGxheU5hbWUiOiJIVE1MLCBDU1MsIEpTIiwidGFnbGluZSI6IlRoZSBsYW5ndWFnZXMgdGhhdCBtYWtlIHVwIHRoZSB3ZWIuIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJoZWFkZXIiOiIiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImV4dCI6Imh0bWwiLCJwcm9qZWN0X3RlbXBsYXRlIjpbeyJuYW1lIjoiaW5kZXguaHRtbCIsImNvbnRlbnQiOiI8IURPQ1RZUEUgaHRtbD5cbjxodG1sPlxuICA8aGVhZD5cbiAgICA8bWV0YSBjaGFyc2V0PVwidXRmLThcIj5cbiAgICA8bWV0YSBuYW1lPVwidmlld3BvcnRcIiBjb250ZW50PVwid2lkdGg9ZGV2aWNlLXdpZHRoXCI+XG4gICAgPHRpdGxlPnJlcGwuaXQ8L3RpdGxlPlxuICAgIDxsaW5rIGhyZWY9XCJpbmRleC5jc3NcIiByZWw9XCJzdHlsZXNoZWV0XCIgdHlwZT1cInRleHQvY3NzXCIgLz5cbiAgPC9oZWFkPlxuICA8Ym9keT5cbiAgICA8c2NyaXB0IHNyYz1cImluZGV4LmpzXCI+PC9zY3JpcHQ+XG4gIDwvYm9keT5cbjwvaHRtbD4iLCJpbmRleCI6MH0seyJuYW1lIjoiaW5kZXguanMiLCJjb250ZW50IjoiIiwiaW5kZXgiOjF9LHsibmFtZSI6ImluZGV4LmNzcyIsImNvbnRlbnQiOiIiLCJpbmRleCI6Mn1dLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3dlYl9wcm9qZWN0LnN2ZyIsImtleSI6IndlYl9wcm9qZWN0In0sImh0bWwiOnsiZW5naW5lIjoicmVwbGJveCIsImRpc3BsYXlOYW1lIjoiSFRNTCwgQ1NTLCBKUyIsInRhZ2xpbmUiOiJUaGUgbGFuZ3VhZ2VzIHRoYXQgbWFrZSB1cCB0aGUgd2ViLiIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiaGVhZGVyIjoiIiwiY2F0ZWdvcnkiOiJXZWIiLCJleHQiOiJodG1sIiwicHJvamVjdF90ZW1wbGF0ZSI6W3sibmFtZSI6ImluZGV4Lmh0bWwiLCJjb250ZW50IjoiPCFET0NUWVBFIGh0bWw+XG48aHRtbD5cbiAgPGhlYWQ+XG4gICAgPG1ldGEgY2hhcnNldD1cInV0Zi04XCI+XG4gICAgPG1ldGEgbmFtZT1cInZpZXdwb3J0XCIgY29udGVudD1cIndpZHRoPWRldmljZS13aWR0aFwiPlxuICAgIDx0aXRsZT5yZXBsLml0PC90aXRsZT5cbiAgICA8bGluayBocmVmPVwiaW5kZXguY3NzXCIgcmVsPVwic3R5bGVzaGVldFwiIHR5cGU9XCJ0ZXh0L2Nzc1wiIC8+XG4gIDwvaGVhZD5cbiAgPGJvZHk+XG4gICAgPHNjcmlwdCBzcmM9XCJpbmRleC5qc1wiPjwvc2NyaXB0PlxuICA8L2JvZHk+XG48L2h0bWw+IiwiaW5kZXgiOjB9LHsibmFtZSI6ImluZGV4LmpzIiwiY29udGVudCI6IiIsImluZGV4IjoxfSx7Im5hbWUiOiJpbmRleC5jc3MiLCJjb250ZW50IjoiIiwiaW5kZXgiOjJ9XSwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy93ZWJfcHJvamVjdC5zdmciLCJrZXkiOiJodG1sIn0sInJ1c3QiOnsiZGlzcGxheU5hbWUiOiJSdXN0IiwidGFnbGluZSI6IkEgZmFzdCBhbmQgc2FmZSBzeXN0ZW1zIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6InJ1c3QiLCJlbnRyeXBvaW50IjoibWFpbi5ycyIsImV4dCI6InJzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJydXN0YyAxLjkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcnVzdC5zdmciLCJ0ZW1wbGF0ZSI6ImZuIG1haW4oKSB7XG4gIHByaW50bG4hKFwiSGVsbG8gV29ybGQhXCIpO1xufSIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwifSwic3dpZnQiOnsiZGlzcGxheU5hbWUiOiJTd2lmdCIsInRhZ2xpbmUiOiJBIG1vZGVybiBnZW5lcmFsLXB1cnBvc2UgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UgZnJvbSBBcHBsZS4iLCJrZXkiOiJzd2lmdCIsImVudHJ5cG9pbnQiOiJtYWluLnN3aWZ0IiwiZXh0Ijoic3dpZnQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6IlN3aWZ0IHZlcnNpb24gMy4wLjEgKFJlbGVhc2UpIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3N3aWZ0LnN2ZyIsInRlbXBsYXRlIjoiIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJweXRob25fdHVydGxlIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uICh3aXRoIFR1cnRsZSkiLCJ0YWdsaW5lIjoiQSBkeW5hbWljIGxhbmd1YWdlIGVtcGhhc2l6aW5nIHJlYWRhYmlsaXR5LiIsImVuZ2luZSI6InB5dGhvbnR1cnRsZSIsImhlYWRlciI6IiIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJleHQiOiJweSIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcHl0aG9uX3R1cnRsZS5zdmciLCJrZXkiOiJweXRob25fdHVydGxlIn0sImplc3QiOnsiZGlzcGxheU5hbWUiOiJKZXN0IiwidGFnbGluZSI6IlBhaW5sZXNzIEphdmFTY3JpcHQgVGVzdGluZy4iLCJrZXkiOiJqZXN0IiwiZW50cnlwb2ludCI6ImNvbmZpZy5qc29uIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6Ikplc3QgdjIyLjEuMiBub2RlIHY3LjQuMCBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiVGVzdGluZyIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamVzdC5zdmciLCJwcm9qZWN0X3RlbXBsYXRlIjpbeyJuYW1lIjoiY29uZmlnLmpzb24iLCJjb250ZW50Ijoie1xuICBcInRlc3RSZWdleFwiOiBcIi4qLXRlc3RcXFxcLmpzJFwiLFxuICBcInRlc3RFbnZpcm9ubWVudFwiOiBcIm5vZGVcIlxufSJ9LHsibmFtZSI6ImFkZC10ZXN0LmpzIiwiY29udGVudCI6ImNvbnN0IGFkZCA9IHJlcXVpcmUoJy4vYWRkJyk7XG5kZXNjcmliZSgnYWRkJywgKCkgPT4ge1xuICBpdCgnc2hvdWxkIGFkZCB0d28gbnVtYmVycycsICgpID0+IHtcbiAgICBleHBlY3QoYWRkKDEsIDIpKS50b0JlKDMpO1xuICB9KTtcbn0pOyJ9LHsibmFtZSI6ImFkZC5qcyIsImNvbnRlbnQiOiJmdW5jdGlvbiBhZGQoYSwgYikge1xuICByZXR1cm4gYSArIGI7XG59XG5cbm1vZHVsZS5leHBvcnRzID0gYWRkOyJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJkamFuZ28iOnsiZGlzcGxheU5hbWUiOiJEamFuZ28iLCJ0YWdsaW5lIjoiUHl0aG9uIGZyYW1ld29yayB0aGF0IGVuY291cmFnZXMgcmFwaWQgZGV2ZWxvcG1lbnQuIiwia2V5IjoiZGphbmdvIiwiZW50cnlwb2ludCI6Im1haW4vdmlld3MucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOnRydWUsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoZWFkZXIiOiJQeXRob24gMy42LjEgKGRlZmF1bHQsIEp1biAyMSAyMDE3LCAxODo0ODozNSlcbltHQ0MgNC45LjJdIG9uIGxpbnV4IiwiY2F0ZWdvcnkiOiJGcmFtZXdvcmsiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2RqYW5nby5zdmciLCJwcm9qZWN0X3RlbXBsYXRlIjpbeyJuYW1lIjoic3RhdGljL2Nzcy9zdHlsZS5jc3MiLCJjb250ZW50IjoiYm9keSB7XG4gICAgYmFja2dyb3VuZDogI2NlY2VjZTtcbn1cbiJ9LHsibmFtZSI6InRlbXBsYXRlcy9iYXNlLmh0bWwiLCJjb250ZW50IjoieyUgbG9hZCBzdGF0aWNmaWxlcyAlfVxuICAgICAgICA8IURPQ1RZUEUgaHRtbD5cblxuPGh0bWwgbGFuZz1cImVuXCI+XG48aGVhZD5cbiAgICA8bWV0YSBjaGFyc2V0PVwiVVRGLThcIj5cbiAgICA8dGl0bGU+SGVsbG8gRGphbmdvPC90aXRsZT5cbiAgICA8bWV0YSBjaGFyc2V0PVwiVVRGLThcIi8+XG4gICAgPG1ldGEgbmFtZT1cInZpZXdwb3J0XCIgY29udGVudD1cIndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xXCIvPlxuICAgIDxsaW5rIHJlbD1cInN0eWxlc2hlZXRcIiBocmVmPVwieyUgc3RhdGljIFwiY3NzL3N0eWxlLmNzc1wiICV9XCI+XG48L2hlYWQ+XG48Ym9keT5cbiAgICB7JSBibG9jayBjb250ZW50ICV9eyUgZW5kYmxvY2sgY29udGVudCAlfVxuPC9ib2R5PlxuPC9odG1sPiJ9LHsibmFtZSI6InRlbXBsYXRlcy9tYWluL2luZGV4Lmh0bWwiLCJjb250ZW50IjoieyUgZXh0ZW5kcyBcImJhc2UuaHRtbFwiICV9XG5cbnslIGJsb2NrIGNvbnRlbnQgJX1cbiAgPGgxPkhlbGxvIFJlcGwuaXQ8L2gxPlxueyUgZW5kYmxvY2sgY29udGVudCAlfSJ9LHsibmFtZSI6Im1haW4vbWlncmF0aW9ucy9fX2luaXRfXy5weSIsImNvbnRlbnQiOiIifSx7Im5hbWUiOiJtYWluL3VybHMucHkiLCJjb250ZW50IjoiZnJvbSBkamFuZ28uY29uZi51cmxzIGltcG9ydCB1cmxcbmZyb20gZGphbmdvLmNvbnRyaWIgaW1wb3J0IGFkbWluXG5mcm9tIG1haW4gaW1wb3J0IHZpZXdzXG5cbnVybHBhdHRlcm5zID0gW1xuICB1cmwocideYWRtaW4vJywgYWRtaW4uc2l0ZS51cmxzKSxcbiAgdXJsKHInXiQnLCB2aWV3cy5ob21lLCBuYW1lPSdob21lJyksXG5dXG4ifSx7Im5hbWUiOiJtYWluL3NldHRpbmdzLnB5IiwiY29udGVudCI6ImltcG9ydCBvc1xuXG5CQVNFX0RJUiA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkpXG5cbiMgU0VDVVJJVFkgV0FSTklORzoga2VlcCB0aGUgc2VjcmV0IGtleSB1c2VkIGluIHByb2R1Y3Rpb24gc2VjcmV0IVxuU0VDUkVUX0tFWSA9ICczM2VsKnZAQCl6aTU3cl9xXzFucmp0YV50cTZuJjhodyh2MXcoPSlhaXcjb2UxcDlkeidcblxuREVCVUcgPSBUcnVlXG5cbiMgU0VDVVJJVFkgV0FSTklORzogbWFrZSBzdXJlIHlvdSB1cGRhdGUgdGhpcyB0byB5b3VyIHdlYnNpdGVzIFVSTFxuQUxMT1dFRF9IT1NUUyA9IFsnKiddXG5YX0ZSQU1FX09QVElPTlMgPSAnQUxMT1cgQUxMJ1xuXG5JTlNUQUxMRURfQVBQUyA9IFtcbiAgICAnZGphbmdvLmNvbnRyaWIuYWRtaW4nLFxuICAgICdkamFuZ28uY29udHJpYi5hdXRoJyxcbiAgICAnZGphbmdvLmNvbnRyaWIuY29udGVudHR5cGVzJyxcbiAgICAnZGphbmdvLmNvbnRyaWIuc2Vzc2lvbnMnLFxuICAgICdkamFuZ28uY29udHJpYi5tZXNzYWdlcycsXG4gICAgJ2RqYW5nby5jb250cmliLnN0YXRpY2ZpbGVzJyxcblxuICAgICdtYWluJyxcbl1cblxuTUlERExFV0FSRSA9IFtcbiAgICAnZGphbmdvLm1pZGRsZXdhcmUuc2VjdXJpdHkuU2VjdXJpdHlNaWRkbGV3YXJlJyxcbiAgICAnZGphbmdvLmNvbnRyaWIuc2Vzc2lvbnMubWlkZGxld2FyZS5TZXNzaW9uTWlkZGxld2FyZScsXG4gICAgJ2RqYW5nby5taWRkbGV3YXJlLmNvbW1vbi5Db21tb25NaWRkbGV3YXJlJyxcbiAgICAnZGphbmdvLm1pZGRsZXdhcmUuY3NyZi5Dc3JmVmlld01pZGRsZXdhcmUnLFxuICAgICdkamFuZ28uY29udHJpYi5hdXRoLm1pZGRsZXdhcmUuQXV0aGVudGljYXRpb25NaWRkbGV3YXJlJyxcbiAgICAnZGphbmdvLmNvbnRyaWIubWVzc2FnZXMubWlkZGxld2FyZS5NZXNzYWdlTWlkZGxld2FyZScsXG4gICAgJ2RqYW5nby5taWRkbGV3YXJlLmNsaWNramFja2luZy5YRnJhbWVPcHRpb25zTWlkZGxld2FyZScsXG5dXG5cblJPT1RfVVJMQ09ORiA9ICdtYWluLnVybHMnXG5cblRFTVBMQVRFUyA9IFtcbiAgICB7XG4gICAgICAgICdCQUNLRU5EJzogJ2RqYW5nby50ZW1wbGF0ZS5iYWNrZW5kcy5kamFuZ28uRGphbmdvVGVtcGxhdGVzJyxcbiAgICAgICAgJ0RJUlMnOiBbb3MucGF0aC5qb2luKEJBU0VfRElSLCAndGVtcGxhdGVzJyldLFxuICAgICAgICAnQVBQX0RJUlMnOiBUcnVlLFxuICAgICAgICAnT1BUSU9OUyc6IHtcbiAgICAgICAgICAgICdjb250ZXh0X3Byb2Nlc3NvcnMnOiBbXG4gICAgICAgICAgICAgICAgJ2RqYW5nby50ZW1wbGF0ZS5jb250ZXh0X3Byb2Nlc3NvcnMuZGVidWcnLFxuICAgICAgICAgICAgICAgICdkamFuZ28udGVtcGxhdGUuY29udGV4dF9wcm9jZXNzb3JzLnJlcXVlc3QnLFxuICAgICAgICAgICAgICAgICdkamFuZ28uY29udHJpYi5hdXRoLmNvbnRleHRfcHJvY2Vzc29ycy5hdXRoJyxcbiAgICAgICAgICAgICAgICAnZGphbmdvLmNvbnRyaWIubWVzc2FnZXMuY29udGV4dF9wcm9jZXNzb3JzLm1lc3NhZ2VzJyxcbiAgICAgICAgICAgIF0sXG4gICAgICAgIH0sXG4gICAgfSxcbl1cblxuV1NHSV9BUFBMSUNBVElPTiA9ICdtYWluLndzZ2kuYXBwbGljYXRpb24nXG5cblxuREFUQUJBU0VTID0ge1xuICAgICdkZWZhdWx0Jzoge1xuICAgICAgICAnRU5HSU5FJzogJ2RqYW5nby5kYi5iYWNrZW5kcy5zcWxpdGUzJyxcbiAgICAgICAgJ05BTUUnOiBvcy5wYXRoLmpvaW4oQkFTRV9ESVIsICdkYi5zcWxpdGUzJyksXG4gICAgfVxufVxuXG5BVVRIX1BBU1NXT1JEX1ZBTElEQVRPUlMgPSBbXG4gICAgeyAnTkFNRSc6ICdkamFuZ28uY29udHJpYi5hdXRoLnBhc3N3b3JkX3ZhbGlkYXRpb24uVXNlckF0dHJpYnV0ZVNpbWlsYXJpdHlWYWxpZGF0b3InIH0sXG4gICAgeyAnTkFNRSc6ICdkamFuZ28uY29udHJpYi5hdXRoLnBhc3N3b3JkX3ZhbGlkYXRpb24uTWluaW11bUxlbmd0aFZhbGlkYXRvcicgfSxcbiAgICB7ICdOQU1FJzogJ2RqYW5nby5jb250cmliLmF1dGgucGFzc3dvcmRfdmFsaWRhdGlvbi5Db21tb25QYXNzd29yZFZhbGlkYXRvcicgfSxcbiAgICB7ICdOQU1FJzogJ2RqYW5nby5jb250cmliLmF1dGgucGFzc3dvcmRfdmFsaWRhdGlvbi5OdW1lcmljUGFzc3dvcmRWYWxpZGF0b3InIH0sXG5dXG5cbkxBTkdVQUdFX0NPREUgPSAnZW4tdXMnXG5USU1FX1pPTkUgPSAnVVRDJ1xuVVNFX0kxOE4gPSBUcnVlXG5VU0VfTDEwTiA9IFRydWVcblVTRV9UWiA9IFRydWVcblxuU1RBVElDX1VSTCA9ICcvc3RhdGljLydcblxuU1RBVElDRklMRVNfRElSUyA9IChcbiAgICBvcy5wYXRoLmpvaW4oQkFTRV9ESVIsICdzdGF0aWMnKSxcbikifSx7Im5hbWUiOiJtYWluL21vZGVscy5weSIsImNvbnRlbnQiOiJmcm9tIGRqYW5nby5kYiBpbXBvcnQgbW9kZWxzXG5cbiMgQ3JlYXRlIHlvdXIgbW9kZWxzIGhlcmUuIn0seyJuYW1lIjoibWFpbi92aWV3cy5weSIsImNvbnRlbnQiOiJmcm9tIGRqYW5nby5zaG9ydGN1dHMgaW1wb3J0IHJlbmRlclxuXG5cbiMgQ3JlYXRlIHlvdXIgdmlld3MgaGVyZS5cbmRlZiBob21lKHJlcXVlc3QpOlxuICAgIHJldHVybiByZW5kZXIocmVxdWVzdCwgJ21haW4vaW5kZXguaHRtbCcpIn1dLCJtYXRjaGluZ3MiOltbInsiLCJ9Il0sWyIoIiwiKSJdLFsiWyIsIl0iXV0sImVuZ2luZSI6ImdvdmFsIiwiY29uZmlnIjp7ImlzU2VydmVyIjp0cnVlfX0sImV4cHJlc3MiOnsiZGlzcGxheU5hbWUiOiJFeHByZXNzIiwidGFnbGluZSI6IkphdmFzY3JpcHQgZnJhbWV3b3JrIGRlc2lnbmVkIGZvciBidWlsZGluZyB3ZWIgYXBwbGljYXRpb25zIGFuZCBBUElzLiIsImtleSI6ImV4cHJlc3MiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoibm9kZSB2OS43LjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkZyYW1ld29yayIsImljb24iOiJodHRwczovL3JlcGwuaXQvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvZXhwcmVzcy5zdmciLCJwcm9qZWN0X3RlbXBsYXRlIjpbeyJuYW1lIjoiZGIuanMiLCJjb250ZW50IjoiY29uc3Qgc3FsaXRlMyA9IHJlcXVpcmUoJ3NxbGl0ZTMnKS52ZXJib3NlKCk7XG5jb25zdCBkYiA9IG5ldyBzcWxpdGUzLkRhdGFiYXNlKCcuL2RiLnNxbGl0ZTMnKTtcblxuZGIucnVuKCdDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyBib29rcyAobmFtZSBURVhULCBhdXRob3IgVEVYVCknKTtcblxubW9kdWxlLmV4cG9ydHMgPSBkYjsifSx7Im5hbWUiOiJwYWNrYWdlLmpzb24iLCJjb250ZW50Ijoie1xuICBcIm5hbWVcIjogXCJhcHBcIixcbiAgXCJ2ZXJzaW9uXCI6IFwiMC4wLjFcIixcbiAgXCJkZXNjcmlwdGlvblwiOiBcIlwiLFxuICBcIm1haW5cIjogXCJpbmRleC5qc1wiLFxuICBcInNjcmlwdHNcIjoge1xuICB9LFxuICBcImF1dGhvclwiOiBcIlwiLFxuICBcImxpY2Vuc2VcIjogXCJNSVRcIixcbiAgXCJkZXBlbmRlbmNpZXNcIjoge1xuICAgIFwiZXhwcmVzc1wiOiBcImxhdGVzdFwiLFxuICAgIFwiYm9keS1wYXJzZXJcIjogXCJsYXRlc3RcIixcbiAgICBcInNxbGl0ZTNcIjogXCJsYXRlc3RcIlxuICB9XG59In0seyJuYW1lIjoiaW5kZXguanMiLCJjb250ZW50IjoiY29uc3QgZXhwcmVzcyA9IHJlcXVpcmUoJ2V4cHJlc3MnKTtcbmNvbnN0IGJvZHlQYXJzZXIgPSByZXF1aXJlKCdib2R5LXBhcnNlcicpO1xuY29uc3QgZGIgPSByZXF1aXJlKCcuL2RiJyk7XG5cbmNvbnN0IGFwcCA9IGV4cHJlc3MoKTtcblxuYXBwLnVzZShib2R5UGFyc2VyLmpzb24oKSk7XG5hcHAudXNlKGJvZHlQYXJzZXIudXJsZW5jb2RlZCh7IGV4dGVuZGVkOiB0cnVlIH0pKTtcblxuYXBwLnVzZShleHByZXNzLnN0YXRpYygncHVibGljJykpO1xuXG5hcHAuZ2V0KCcvJywgKHJlcSwgcmVzKSA9PiB7XG5cdHJlcy5zZW5kKCdIZWxsbyBFeHByZXNzIGFwcCcpO1xufSk7XG5cbmFwcC5saXN0ZW4oMzAwMCwgKCkgPT4gY29uc29sZS5sb2coJ3NlcnZlciBzdGFydGVkJykpOyJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJzaW5hdHJhIjp7ImRpc3BsYXlOYW1lIjoiU2luYXRyYSIsInRhZ2xpbmUiOiJEU0wgZm9yIHF1aWNrbHkgY3JlYXRpbmcgd2ViIGFwcGxpY2F0aW9ucyBpbiBSdWJ5IHdpdGggbWluaW1hbCBlZmZvcnQiLCJrZXkiOiJzaW5hdHJhIiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoicnVieSAyLjUuMHAwICgyMDE3LTEyLTI1IHJldmlzaW9uIDYxNDY4KSBbeDg2XzY0LWxpbnV4XSIsImNhdGVnb3J5IjoiRnJhbWV3b3JrIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9zaW5hdHJhLnBuZyIsInByb2plY3RfdGVtcGxhdGUiOlt7Im5hbWUiOiJ2aWV3cy9pbmRleC5lcmIiLCJjb250ZW50IjoiXG48IURPQ1RZUEUgaHRtbD5cbjxodG1sIGxhbmc9XCJlblwiPlxuPGhlYWQ+XG4gIDx0aXRsZT5IZWxsbyE8L3RpdGxlPlxuPC9oZWFkPlxuPGJvZHk+XG4gIEhlbGxvIGZyb20gPCU9IGhvc3QgJT4uXG48L2JvZHk+XG48L2h0bWw+In0seyJuYW1lIjoiR2VtZmlsZSIsImNvbnRlbnQiOiJzb3VyY2UgJ2h0dHA6Ly9ydWJ5Z2Vtcy5vcmcnXG5cbmdlbSAnc2luYXRyYScifSx7Im5hbWUiOiJtYWluLnJiIiwiY29udGVudCI6InJlcXVpcmUgJ3NpbmF0cmEnXG5cbnNldCA6cHJvdGVjdGlvbiwgOmV4Y2VwdCA9PiA6ZnJhbWVfb3B0aW9uc1xuc2V0IDpiaW5kLCAnMC4wLjAuMCdcblxuZ2V0ICcvJyBkb1xuICBlcmIgOmluZGV4LCA6bG9jYWxzID0+IHsgaG9zdDogcmVxdWVzdC5ob3N0IH1cbmVuZCJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJyYWlscyI6eyJkaXNwbGF5TmFtZSI6IlJ1Ynkgb24gUmFpbHMiLCJ0YWdsaW5lIjoiQSB3ZWItYXBwbGljYXRpb24gZnJhbWV3b3JrIHRoYXQgaW5jbHVkZXMgZXZlcnl0aGluZyBuZWVkZWQgdG8gY3JlYXRlIHdlYiBhcHBsaWNhdGlvbnMiLCJrZXkiOiJyYWlscyIsImVudHJ5cG9pbnQiOiJjb25maWcvcm91dGVzLnJiIiwiZXh0IjoicmIiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJydWJ5IDIuNS4wcDAgKDIwMTctMTItMjUgcmV2aXNpb24gNjE0NjgpIFt4ODZfNjQtbGludXhdIiwiY2F0ZWdvcnkiOiJGcmFtZXdvcmsiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JhaWxzLnN2ZyIsInByb2plY3RfdGVtcGxhdGUiOlt7Im5hbWUiOiJHZW1maWxlIiwiY29udGVudCI6InNvdXJjZSAnaHR0cHM6Ly9ydWJ5Z2Vtcy5vcmcnXG5naXRfc291cmNlKDpnaXRodWIpIHsgfHJlcG98IFwiaHR0cHM6Ly9naXRodWIuY29tLyN7cmVwb30uZ2l0XCIgfVxuXG5ydWJ5ICcyLjUuMSdcblxuIyBCdW5kbGUgZWRnZSBSYWlscyBpbnN0ZWFkOiBnZW0gJ3JhaWxzJywgZ2l0aHViOiAncmFpbHMvcmFpbHMnXG5nZW0gJ3JhaWxzJywgJ34+IDUuMi4wJ1xuIyBVc2Ugc3FsaXRlMyBhcyB0aGUgZGF0YWJhc2UgZm9yIEFjdGl2ZSBSZWNvcmRcbmdlbSAnc3FsaXRlMydcbiMgQnVpbGQgSlNPTiBBUElzIHdpdGggZWFzZS4gUmVhZCBtb3JlOiBodHRwczovL2dpdGh1Yi5jb20vcmFpbHMvamJ1aWxkZXJcbmdlbSAnamJ1aWxkZXInLCAnfj4gMi41J1xuIyBVc2UgQWN0aXZlTW9kZWwgaGFzX3NlY3VyZV9wYXNzd29yZFxuIyBnZW0gJ2JjcnlwdCcsICd+PiAzLjEuNydcblxuIyBVc2UgQWN0aXZlU3RvcmFnZSB2YXJpYW50XG4jIGdlbSAnbWluaV9tYWdpY2snLCAnfj4gNC44J1xuXG4jIFVzZSBDYXBpc3RyYW5vIGZvciBkZXBsb3ltZW50XG4jIGdlbSAnY2FwaXN0cmFuby1yYWlscycsIGdyb3VwOiA6ZGV2ZWxvcG1lbnRcblxuIyBSZWR1Y2VzIGJvb3QgdGltZXMgdGhyb3VnaCBjYWNoaW5nOyByZXF1aXJlZCBpbiBjb25maWcvYm9vdC5yYlxuZ2VtICdib290c25hcCcsICc+PSAxLjEuMCcsIHJlcXVpcmU6IGZhbHNlXG5cbmdyb3VwIDpkZXZlbG9wbWVudCwgOnRlc3QgZG9cbiAgIyBDYWxsICdieWVidWcnIGFueXdoZXJlIGluIHRoZSBjb2RlIHRvIHN0b3AgZXhlY3V0aW9uIGFuZCBnZXQgYSBkZWJ1Z2dlciBjb25zb2xlXG4gIGdlbSAnYnllYnVnJywgcGxhdGZvcm1zOiBbOm1yaSwgOm1pbmd3LCA6eDY0X21pbmd3XVxuZW5kXG5cbmdyb3VwIDpkZXZlbG9wbWVudCBkb1xuICAjIEFjY2VzcyBhbiBpbnRlcmFjdGl2ZSBjb25zb2xlIG9uIGV4Y2VwdGlvbiBwYWdlcyBvciBieSBjYWxsaW5nICdjb25zb2xlJyBhbnl3aGVyZSBpbiB0aGUgY29kZS5cbiAgZ2VtICd3ZWItY29uc29sZScsICc+PSAzLjMuMCdcbmVuZFxuXG5cbiMgV2luZG93cyBkb2VzIG5vdCBpbmNsdWRlIHpvbmVpbmZvIGZpbGVzLCBzbyBidW5kbGUgdGhlIHR6aW5mby1kYXRhIGdlbVxuZ2VtICd0emluZm8tZGF0YScsIHBsYXRmb3JtczogWzptaW5ndywgOm1zd2luLCA6eDY0X21pbmd3LCA6anJ1YnldXG4ifSx7Im5hbWUiOiJjb25maWcvYm9vdC5yYiIsImNvbnRlbnQiOiJFTlZbJ0JVTkRMRV9HRU1GSUxFJ10gfHw9IEZpbGUuZXhwYW5kX3BhdGgoJy4uL0dlbWZpbGUnLCBfX2Rpcl9fKVxuXG5yZXF1aXJlICdidW5kbGVyL3NldHVwJyAjIFNldCB1cCBnZW1zIGxpc3RlZCBpbiB0aGUgR2VtZmlsZS5cbnJlcXVpcmUgJ2Jvb3RzbmFwL3NldHVwJyAjIFNwZWVkIHVwIGJvb3QgdGltZSBieSBjYWNoaW5nIGV4cGVuc2l2ZSBvcGVyYXRpb25zLlxuIn0seyJuYW1lIjoiY29uZmlnL3JvdXRlcy5yYiIsImNvbnRlbnQiOiJSYWlscy5hcHBsaWNhdGlvbi5yb3V0ZXMuZHJhdyBkb1xuICAjIEZvciBkZXRhaWxzIG9uIHRoZSBEU0wgYXZhaWxhYmxlIHdpdGhpbiB0aGlzIGZpbGUsIHNlZSBodHRwOi8vZ3VpZGVzLnJ1YnlvbnJhaWxzLm9yZy9yb3V0aW5nLmh0bWxcbmVuZFxuIn0seyJuYW1lIjoiY29uZmlnL2RhdGFiYXNlLnltbCIsImNvbnRlbnQiOiIjIFNRTGl0ZSB2ZXJzaW9uIDMueFxuIyAgIGdlbSBpbnN0YWxsIHNxbGl0ZTNcbiNcbiMgICBFbnN1cmUgdGhlIFNRTGl0ZSAzIGdlbSBpcyBkZWZpbmVkIGluIHlvdXIgR2VtZmlsZVxuIyAgIGdlbSAnc3FsaXRlMydcbiNcbmRlZmF1bHQ6ICZkZWZhdWx0XG4gIGFkYXB0ZXI6IHNxbGl0ZTNcbiAgcG9vbDogPCU9IEVOVi5mZXRjaChcIlJBSUxTX01BWF9USFJFQURTXCIpIHsgNSB9ICU+XG4gIHRpbWVvdXQ6IDUwMDBcblxuZGV2ZWxvcG1lbnQ6XG4gIDw8OiAqZGVmYXVsdFxuICBkYXRhYmFzZTogZGIvZGV2ZWxvcG1lbnQuc3FsaXRlM1xuXG4jIFdhcm5pbmc6IFRoZSBkYXRhYmFzZSBkZWZpbmVkIGFzIFwidGVzdFwiIHdpbGwgYmUgZXJhc2VkIGFuZFxuIyByZS1nZW5lcmF0ZWQgZnJvbSB5b3VyIGRldmVsb3BtZW50IGRhdGFiYXNlIHdoZW4geW91IHJ1biBcInJha2VcIi5cbiMgRG8gbm90IHNldCB0aGlzIGRiIHRvIHRoZSBzYW1lIGFzIGRldmVsb3BtZW50IG9yIHByb2R1Y3Rpb24uXG50ZXN0OlxuICA8PDogKmRlZmF1bHRcbiAgZGF0YWJhc2U6IGRiL3Rlc3Quc3FsaXRlM1xuXG5wcm9kdWN0aW9uOlxuICA8PDogKmRlZmF1bHRcbiAgZGF0YWJhc2U6IGRiL3Byb2R1Y3Rpb24uc3FsaXRlM1xuIn0seyJuYW1lIjoiY29uZmlnL2FwcGxpY2F0aW9uLnJiIiwiY29udGVudCI6InJlcXVpcmVfcmVsYXRpdmUgXCJib290XCJcblxucmVxdWlyZSBcInJhaWxzXCJcbiMgUGljayB0aGUgZnJhbWV3b3JrcyB5b3Ugd2FudDpcbnJlcXVpcmUgXCJhY3RpdmVfbW9kZWwvcmFpbHRpZVwiXG5yZXF1aXJlIFwiYWN0aXZlX2pvYi9yYWlsdGllXCJcbnJlcXVpcmUgXCJhY3RpdmVfcmVjb3JkL3JhaWx0aWVcIlxucmVxdWlyZSBcImFjdGl2ZV9zdG9yYWdlL2VuZ2luZVwiXG5yZXF1aXJlIFwiYWN0aW9uX2NvbnRyb2xsZXIvcmFpbHRpZVwiXG4jIHJlcXVpcmUgXCJhY3Rpb25fbWFpbGVyL3JhaWx0aWVcIlxucmVxdWlyZSBcImFjdGlvbl92aWV3L3JhaWx0aWVcIlxuIyByZXF1aXJlIFwiYWN0aW9uX2NhYmxlL2VuZ2luZVwiXG4jIHJlcXVpcmUgXCJzcHJvY2tldHMvcmFpbHRpZVwiXG4jIHJlcXVpcmUgXCJyYWlscy90ZXN0X3VuaXQvcmFpbHRpZVwiXG5cbiMgUmVxdWlyZSB0aGUgZ2VtcyBsaXN0ZWQgaW4gR2VtZmlsZSwgaW5jbHVkaW5nIGFueSBnZW1zXG4jIHlvdSd2ZSBsaW1pdGVkIHRvIDp0ZXN0LCA6ZGV2ZWxvcG1lbnQsIG9yIDpwcm9kdWN0aW9uLlxuQnVuZGxlci5yZXF1aXJlKCpSYWlscy5ncm91cHMpXG5cbm1vZHVsZSBBcHBcbiAgY2xhc3MgQXBwbGljYXRpb24gPCBSYWlsczo6QXBwbGljYXRpb25cbiAgICBjb25maWcuYWN0aW9uX2Rpc3BhdGNoLmRlZmF1bHRfaGVhZGVycyA9IHtcbiAgICAgIFwiWC1GcmFtZS1PcHRpb25zXCIgPT4gXCJBTExPV0FMTFwiLFxuICAgIH1cblxuICAgICMgSW5pdGlhbGl6ZSBjb25maWd1cmF0aW9uIGRlZmF1bHRzIGZvciBvcmlnaW5hbGx5IGdlbmVyYXRlZCBSYWlscyB2ZXJzaW9uLlxuICAgIGNvbmZpZy5sb2FkX2RlZmF1bHRzIDUuMlxuXG4gICAgIyBTZXR0aW5ncyBpbiBjb25maWcvZW52aXJvbm1lbnRzLyogdGFrZSBwcmVjZWRlbmNlIG92ZXIgdGhvc2Ugc3BlY2lmaWVkIGhlcmUuXG4gICAgIyBBcHBsaWNhdGlvbiBjb25maWd1cmF0aW9uIGNhbiBnbyBpbnRvIGZpbGVzIGluIGNvbmZpZy9pbml0aWFsaXplcnNcbiAgICAjIC0tIGFsbCAucmIgZmlsZXMgaW4gdGhhdCBkaXJlY3RvcnkgYXJlIGF1dG9tYXRpY2FsbHkgbG9hZGVkIGFmdGVyIGxvYWRpbmdcbiAgICAjIHRoZSBmcmFtZXdvcmsgYW5kIGFueSBnZW1zIGluIHlvdXIgYXBwbGljYXRpb24uXG5cbiAgICAjIERvbid0IGdlbmVyYXRlIHN5c3RlbSB0ZXN0IGZpbGVzLlxuICAgIGNvbmZpZy5nZW5lcmF0b3JzLnN5c3RlbV90ZXN0cyA9IG5pbFxuICBlbmRcbmVuZFxuIn0seyJuYW1lIjoicHVibGljLzQwNC5odG1sIiwiY29udGVudCI6IjwhRE9DVFlQRSBodG1sPlxuPGh0bWw+XG48aGVhZD5cbiAgPHRpdGxlPlRoZSBwYWdlIHlvdSB3ZXJlIGxvb2tpbmcgZm9yIGRvZXNuJ3QgZXhpc3QgKDQwNCk8L3RpdGxlPlxuICA8bWV0YSBuYW1lPVwidmlld3BvcnRcIiBjb250ZW50PVwid2lkdGg9ZGV2aWNlLXdpZHRoLGluaXRpYWwtc2NhbGU9MVwiPlxuICA8c3R5bGU+XG4gIC5yYWlscy1kZWZhdWx0LWVycm9yLXBhZ2Uge1xuICAgIGJhY2tncm91bmQtY29sb3I6ICNFRkVGRUY7XG4gICAgY29sb3I6ICMyRTJGMzA7XG4gICAgdGV4dC1hbGlnbjogY2VudGVyO1xuICAgIGZvbnQtZmFtaWx5OiBhcmlhbCwgc2Fucy1zZXJpZjtcbiAgICBtYXJnaW46IDA7XG4gIH1cblxuICAucmFpbHMtZGVmYXVsdC1lcnJvci1wYWdlIGRpdi5kaWFsb2cge1xuICAgIHdpZHRoOiA5NSU7XG4gICAgbWF4LXdpZHRoOiAzM2VtO1xuICAgIG1hcmdpbjogNGVtIGF1dG8gMDtcbiAgfVxuXG4gIC5yYWlscy1kZWZhdWx0LWVycm9yLXBhZ2UgZGl2LmRpYWxvZyA+IGRpdiB7XG4gICAgYm9yZGVyOiAxcHggc29saWQgI0NDQztcbiAgICBib3JkZXItcmlnaHQtY29sb3I6ICM5OTk7XG4gICAgYm9yZGVyLWxlZnQtY29sb3I6ICM5OTk7XG4gICAgYm9yZGVyLWJvdHRvbS1jb2xvcjogI0JCQjtcbiAgICBib3JkZXItdG9wOiAjQjAwMTAwIHNvbGlkIDRweDtcbiAgICBib3JkZXItdG9wLWxlZnQtcmFkaXVzOiA5cHg7XG4gICAgYm9yZGVyLXRvcC1yaWdodC1yYWRpdXM6IDlweDtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiB3aGl0ZTtcbiAgICBwYWRkaW5nOiA3cHggMTIlIDA7XG4gICAgYm94LXNoYWRvdzogMCAzcHggOHB4IHJnYmEoNTAsIDUwLCA1MCwgMC4xNyk7XG4gIH1cblxuICAucmFpbHMtZGVmYXVsdC1lcnJvci1wYWdlIGgxIHtcbiAgICBmb250LXNpemU6IDEwMCU7XG4gICAgY29sb3I6ICM3MzBFMTU7XG4gICAgbGluZS1oZWlnaHQ6IDEuNWVtO1xuICB9XG5cbiAgLnJhaWxzLWRlZmF1bHQtZXJyb3ItcGFnZSBkaXYuZGlhbG9nID4gcCB7XG4gICAgbWFyZ2luOiAwIDAgMWVtO1xuICAgIHBhZGRpbmc6IDFlbTtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjRjdGN0Y3O1xuICAgIGJvcmRlcjogMXB4IHNvbGlkICNDQ0M7XG4gICAgYm9yZGVyLXJpZ2h0LWNvbG9yOiAjOTk5O1xuICAgIGJvcmRlci1sZWZ0LWNvbG9yOiAjOTk5O1xuICAgIGJvcmRlci1ib3R0b20tY29sb3I6ICM5OTk7XG4gICAgYm9yZGVyLWJvdHRvbS1sZWZ0LXJhZGl1czogNHB4O1xuICAgIGJvcmRlci1ib3R0b20tcmlnaHQtcmFkaXVzOiA0cHg7XG4gICAgYm9yZGVyLXRvcC1jb2xvcjogI0RBREFEQTtcbiAgICBjb2xvcjogIzY2NjtcbiAgICBib3gtc2hhZG93OiAwIDNweCA4cHggcmdiYSg1MCwgNTAsIDUwLCAwLjE3KTtcbiAgfVxuICA8L3N0eWxlPlxuPC9oZWFkPlxuXG48Ym9keSBjbGFzcz1cInJhaWxzLWRlZmF1bHQtZXJyb3ItcGFnZVwiPlxuICA8IS0tIFRoaXMgZmlsZSBsaXZlcyBpbiBwdWJsaWMvNDA0Lmh0bWwgLS0+XG4gIDxkaXYgY2xhc3M9XCJkaWFsb2dcIj5cbiAgICA8ZGl2PlxuICAgICAgPGgxPlRoZSBwYWdlIHlvdSB3ZXJlIGxvb2tpbmcgZm9yIGRvZXNuJ3QgZXhpc3QuPC9oMT5cbiAgICAgIDxwPllvdSBtYXkgaGF2ZSBtaXN0eXBlZCB0aGUgYWRkcmVzcyBvciB0aGUgcGFnZSBtYXkgaGF2ZSBtb3ZlZC48L3A+XG4gICAgPC9kaXY+XG4gICAgPHA+SWYgeW91IGFyZSB0aGUgYXBwbGljYXRpb24gb3duZXIgY2hlY2sgdGhlIGxvZ3MgZm9yIG1vcmUgaW5mb3JtYXRpb24uPC9wPlxuICA8L2Rpdj5cbjwvYm9keT5cbjwvaHRtbD5cbiJ9LHsibmFtZSI6InB1YmxpYy81MDAuaHRtbCIsImNvbnRlbnQiOiI8IURPQ1RZUEUgaHRtbD5cbjxodG1sPlxuPGhlYWQ+XG4gIDx0aXRsZT5XZSdyZSBzb3JyeSwgYnV0IHNvbWV0aGluZyB3ZW50IHdyb25nICg1MDApPC90aXRsZT5cbiAgPG1ldGEgbmFtZT1cInZpZXdwb3J0XCIgY29udGVudD1cIndpZHRoPWRldmljZS13aWR0aCxpbml0aWFsLXNjYWxlPTFcIj5cbiAgPHN0eWxlPlxuICAucmFpbHMtZGVmYXVsdC1lcnJvci1wYWdlIHtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjRUZFRkVGO1xuICAgIGNvbG9yOiAjMkUyRjMwO1xuICAgIHRleHQtYWxpZ246IGNlbnRlcjtcbiAgICBmb250LWZhbWlseTogYXJpYWwsIHNhbnMtc2VyaWY7XG4gICAgbWFyZ2luOiAwO1xuICB9XG5cbiAgLnJhaWxzLWRlZmF1bHQtZXJyb3ItcGFnZSBkaXYuZGlhbG9nIHtcbiAgICB3aWR0aDogOTUlO1xuICAgIG1heC13aWR0aDogMzNlbTtcbiAgICBtYXJnaW46IDRlbSBhdXRvIDA7XG4gIH1cblxuICAucmFpbHMtZGVmYXVsdC1lcnJvci1wYWdlIGRpdi5kaWFsb2cgPiBkaXYge1xuICAgIGJvcmRlcjogMXB4IHNvbGlkICNDQ0M7XG4gICAgYm9yZGVyLXJpZ2h0LWNvbG9yOiAjOTk5O1xuICAgIGJvcmRlci1sZWZ0LWNvbG9yOiAjOTk5O1xuICAgIGJvcmRlci1ib3R0b20tY29sb3I6ICNCQkI7XG4gICAgYm9yZGVyLXRvcDogI0IwMDEwMCBzb2xpZCA0cHg7XG4gICAgYm9yZGVyLXRvcC1sZWZ0LXJhZGl1czogOXB4O1xuICAgIGJvcmRlci10b3AtcmlnaHQtcmFkaXVzOiA5cHg7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogd2hpdGU7XG4gICAgcGFkZGluZzogN3B4IDEyJSAwO1xuICAgIGJveC1zaGFkb3c6IDAgM3B4IDhweCByZ2JhKDUwLCA1MCwgNTAsIDAuMTcpO1xuICB9XG5cbiAgLnJhaWxzLWRlZmF1bHQtZXJyb3ItcGFnZSBoMSB7XG4gICAgZm9udC1zaXplOiAxMDAlO1xuICAgIGNvbG9yOiAjNzMwRTE1O1xuICAgIGxpbmUtaGVpZ2h0OiAxLjVlbTtcbiAgfVxuXG4gIC5yYWlscy1kZWZhdWx0LWVycm9yLXBhZ2UgZGl2LmRpYWxvZyA+IHAge1xuICAgIG1hcmdpbjogMCAwIDFlbTtcbiAgICBwYWRkaW5nOiAxZW07XG4gICAgYmFja2dyb3VuZC1jb2xvcjogI0Y3RjdGNztcbiAgICBib3JkZXI6IDFweCBzb2xpZCAjQ0NDO1xuICAgIGJvcmRlci1yaWdodC1jb2xvcjogIzk5OTtcbiAgICBib3JkZXItbGVmdC1jb2xvcjogIzk5OTtcbiAgICBib3JkZXItYm90dG9tLWNvbG9yOiAjOTk5O1xuICAgIGJvcmRlci1ib3R0b20tbGVmdC1yYWRpdXM6IDRweDtcbiAgICBib3JkZXItYm90dG9tLXJpZ2h0LXJhZGl1czogNHB4O1xuICAgIGJvcmRlci10b3AtY29sb3I6ICNEQURBREE7XG4gICAgY29sb3I6ICM2NjY7XG4gICAgYm94LXNoYWRvdzogMCAzcHggOHB4IHJnYmEoNTAsIDUwLCA1MCwgMC4xNyk7XG4gIH1cbiAgPC9zdHlsZT5cbjwvaGVhZD5cblxuPGJvZHkgY2xhc3M9XCJyYWlscy1kZWZhdWx0LWVycm9yLXBhZ2VcIj5cbiAgPCEtLSBUaGlzIGZpbGUgbGl2ZXMgaW4gcHVibGljLzUwMC5odG1sIC0tPlxuICA8ZGl2IGNsYXNzPVwiZGlhbG9nXCI+XG4gICAgPGRpdj5cbiAgICAgIDxoMT5XZSdyZSBzb3JyeSwgYnV0IHNvbWV0aGluZyB3ZW50IHdyb25nLjwvaDE+XG4gICAgPC9kaXY+XG4gICAgPHA+SWYgeW91IGFyZSB0aGUgYXBwbGljYXRpb24gb3duZXIgY2hlY2sgdGhlIGxvZ3MgZm9yIG1vcmUgaW5mb3JtYXRpb24uPC9wPlxuICA8L2Rpdj5cbjwvYm9keT5cbjwvaHRtbD5cbiJ9LHsibmFtZSI6ImFwcC92aWV3cy9sYXlvdXRzL2FwcGxpY2F0aW9uLmh0bWwuZXJiIiwiY29udGVudCI6IjwhRE9DVFlQRSBodG1sPlxuPGh0bWw+XG4gIDxoZWFkPlxuICAgIDx0aXRsZT5BcHA8L3RpdGxlPlxuICAgIDwlPSBjc3JmX21ldGFfdGFncyAlPlxuICAgIDwlPSBjc3BfbWV0YV90YWcgJT5cblxuICAgIDwlPSBzdHlsZXNoZWV0X2xpbmtfdGFnICAgICdhcHBsaWNhdGlvbicsIG1lZGlhOiAnYWxsJyAlPlxuICAgIDwlPSBqYXZhc2NyaXB0X2luY2x1ZGVfdGFnICdhcHBsaWNhdGlvbicgJT5cbiAgPC9oZWFkPlxuXG4gIDxib2R5PlxuICAgIDwlPSB5aWVsZCAlPlxuICA8L2JvZHk+XG48L2h0bWw+XG4ifSx7Im5hbWUiOiJhcHAvbW9kZWxzL2FwcGxpY2F0aW9uX3JlY29yZC5yYiIsImNvbnRlbnQiOiJjbGFzcyBBcHBsaWNhdGlvblJlY29yZCA8IEFjdGl2ZVJlY29yZDo6QmFzZVxuICBzZWxmLmFic3RyYWN0X2NsYXNzID0gdHJ1ZVxuZW5kXG4ifSx7Im5hbWUiOiJhcHAvYXNzZXRzL2NvbmZpZy9tYW5pZmVzdC5qcyIsImNvbnRlbnQiOiIvLz0gbGlua190cmVlIC4uL2ltYWdlc1xuLy89IGxpbmtfZGlyZWN0b3J5IC4uL2phdmFzY3JpcHRzIC5qc1xuLy89IGxpbmtfZGlyZWN0b3J5IC4uL3N0eWxlc2hlZXRzIC5jc3NcbiJ9LHsibmFtZSI6ImFwcC9hc3NldHMvamF2YXNjcmlwdHMvYXBwbGljYXRpb24uanMiLCJjb250ZW50IjoiLy8gVGhpcyBpcyBhIG1hbmlmZXN0IGZpbGUgdGhhdCdsbCBiZSBjb21waWxlZCBpbnRvIGFwcGxpY2F0aW9uLmpzLCB3aGljaCB3aWxsIGluY2x1ZGUgYWxsIHRoZSBmaWxlc1xuLy8gbGlzdGVkIGJlbG93LlxuLy9cbi8vIEFueSBKYXZhU2NyaXB0L0NvZmZlZSBmaWxlIHdpdGhpbiB0aGlzIGRpcmVjdG9yeSwgbGliL2Fzc2V0cy9qYXZhc2NyaXB0cywgb3IgYW55IHBsdWdpbidzXG4vLyB2ZW5kb3IvYXNzZXRzL2phdmFzY3JpcHRzIGRpcmVjdG9yeSBjYW4gYmUgcmVmZXJlbmNlZCBoZXJlIHVzaW5nIGEgcmVsYXRpdmUgcGF0aC5cbi8vXG4vLyBJdCdzIG5vdCBhZHZpc2FibGUgdG8gYWRkIGNvZGUgZGlyZWN0bHkgaGVyZSwgYnV0IGlmIHlvdSBkbywgaXQnbGwgYXBwZWFyIGF0IHRoZSBib3R0b20gb2YgdGhlXG4vLyBjb21waWxlZCBmaWxlLiBKYXZhU2NyaXB0IGNvZGUgaW4gdGhpcyBmaWxlIHNob3VsZCBiZSBhZGRlZCBhZnRlciB0aGUgbGFzdCByZXF1aXJlXyogc3RhdGVtZW50LlxuLy9cbi8vIFJlYWQgU3Byb2NrZXRzIFJFQURNRSAoaHR0cHM6Ly9naXRodWIuY29tL3JhaWxzL3Nwcm9ja2V0cyNzcHJvY2tldHMtZGlyZWN0aXZlcykgZm9yIGRldGFpbHNcbi8vIGFib3V0IHN1cHBvcnRlZCBkaXJlY3RpdmVzLlxuLy9cbi8vPSByZXF1aXJlIHJhaWxzLXVqc1xuLy89IHJlcXVpcmUgYWN0aXZlc3RvcmFnZVxuLy89IHJlcXVpcmVfdHJlZSAuXG4ifSx7Im5hbWUiOiJhcHAvYXNzZXRzL3N0eWxlc2hlZXRzL2FwcGxpY2F0aW9uLmNzcyIsImNvbnRlbnQiOiIvKlxuICogVGhpcyBpcyBhIG1hbmlmZXN0IGZpbGUgdGhhdCdsbCBiZSBjb21waWxlZCBpbnRvIGFwcGxpY2F0aW9uLmNzcywgd2hpY2ggd2lsbCBpbmNsdWRlIGFsbCB0aGUgZmlsZXNcbiAqIGxpc3RlZCBiZWxvdy5cbiAqXG4gKiBBbnkgQ1NTIGFuZCBTQ1NTIGZpbGUgd2l0aGluIHRoaXMgZGlyZWN0b3J5LCBsaWIvYXNzZXRzL3N0eWxlc2hlZXRzLCBvciBhbnkgcGx1Z2luJ3NcbiAqIHZlbmRvci9hc3NldHMvc3R5bGVzaGVldHMgZGlyZWN0b3J5IGNhbiBiZSByZWZlcmVuY2VkIGhlcmUgdXNpbmcgYSByZWxhdGl2ZSBwYXRoLlxuICpcbiAqIFlvdSdyZSBmcmVlIHRvIGFkZCBhcHBsaWNhdGlvbi13aWRlIHN0eWxlcyB0byB0aGlzIGZpbGUgYW5kIHRoZXknbGwgYXBwZWFyIGF0IHRoZSBib3R0b20gb2YgdGhlXG4gKiBjb21waWxlZCBmaWxlIHNvIHRoZSBzdHlsZXMgeW91IGFkZCBoZXJlIHRha2UgcHJlY2VkZW5jZSBvdmVyIHN0eWxlcyBkZWZpbmVkIGluIGFueSBvdGhlciBDU1MvU0NTU1xuICogZmlsZXMgaW4gdGhpcyBkaXJlY3RvcnkuIFN0eWxlcyBpbiB0aGlzIGZpbGUgc2hvdWxkIGJlIGFkZGVkIGFmdGVyIHRoZSBsYXN0IHJlcXVpcmVfKiBzdGF0ZW1lbnQuXG4gKiBJdCBpcyBnZW5lcmFsbHkgYmV0dGVyIHRvIGNyZWF0ZSBhIG5ldyBmaWxlIHBlciBzdHlsZSBzY29wZS5cbiAqXG4gKj0gcmVxdWlyZV90cmVlIC5cbiAqPSByZXF1aXJlX3NlbGZcbiAqL1xuIn0seyJuYW1lIjoiYXBwL2NvbnRyb2xsZXJzL2FwcGxpY2F0aW9uX2NvbnRyb2xsZXIucmIiLCJjb250ZW50IjoiY2xhc3MgQXBwbGljYXRpb25Db250cm9sbGVyIDwgQWN0aW9uQ29udHJvbGxlcjo6QmFzZVxuZW5kXG4ifSx7Im5hbWUiOiJhcHAvaGVscGVycy9hcHBsaWNhdGlvbl9oZWxwZXIucmIiLCJjb250ZW50IjoibW9kdWxlIEFwcGxpY2F0aW9uSGVscGVyXG5lbmRcbiJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJybGFuZyI6eyJkaXNwbGF5TmFtZSI6IlIiLCJ0YWdsaW5lIjoiYSBwcm9ncmFtbWluZyBsYW5ndWFnZSBhbmQgZW52aXJvbm1lbnQgZm9yIHN0YXRpc3RpY2FsIGNvbXB1dGluZyBhbmQgZ3JhcGhpY3MiLCJrZXkiOiJybGFuZyIsImVudHJ5cG9pbnQiOiJtYWluLnIiLCJleHQiOiJyIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJ1c2luZyBHTlUgUiBWZXJzaW9uIDMuNS4wICgyMDE4LTA0LTIzKSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ybGFuZy5zdmciLCJ0ZW1wbGF0ZSI6IiIsIm1hdGNoaW5ncyI6W10sImVuZ2luZSI6ImdvdmFsIn0sIm5leHRqcyI6eyJkaXNwbGF5TmFtZSI6Ik5leHQuanMiLCJ0YWdsaW5lIjoiQSBsaWdodHdlaWdodCBmcmFtZXdvcmsgZm9yIHN0YXRpYyBhbmQgc2VydmVyXHUyMDExcmVuZGVyZWQgUmVhY3QgYXBwbGljYXRpb25zIiwia2V5IjoibmV4dGpzIiwiZW50cnlwb2ludCI6InBhZ2VzL2luZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJOZXh0LmpzIDYuMC4zLCBub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiRnJhbWV3b3JrIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwicHJvamVjdF90ZW1wbGF0ZSI6W3sibmFtZSI6InBhZ2VzL2luZGV4LmpzIiwiY29udGVudCI6ImV4cG9ydCBkZWZhdWx0ICgpID0+IDxkaXY+V2VsY29tZSB0byBuZXh0LmpzITwvZGl2PjsifSx7Im5hbWUiOiJwYWNrYWdlLmpzb24iLCJjb250ZW50Ijoie1xuICBcIm5hbWVcIjogXCJteS1hd2Vzb21lLWFwcFwiLFxuICBcInZlcnNpb25cIjogXCIxLjAuMFwiLFxuICBcImRlc2NyaXB0aW9uXCI6IFwiZWFzaWx5IHRoZSBuZXh0IGZhY2Vib29rXCIsXG4gIFwia2V5d29yZHNcIjogW10sXG4gIFwiZGVwZW5kZW5jaWVzXCI6IHtcbiAgICBcInJlYWN0XCI6IFwiMTYuNC4wXCIsXG4gICAgXCJyZWFjdC1kb21cIjogXCIxNi40XCIsXG4gICAgXCJuZXh0XCI6IFwiNi4wLjNcIlxuICB9LFxuICBcImRldkRlcGVuZGVuY2llc1wiOiB7fSxcbiAgXCJzY3JpcHRzXCI6IHtcbiAgICBcImRldlwiOiBcIm5leHRcIixcbiAgICBcImJ1aWxkXCI6IFwibmV4dCBidWlsZFwiLFxuICAgIFwic3RhcnRcIjogXCJuZXh0IHN0YXJ0XCJcbiAgfVxufSJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJnYXRzYnlqcyI6eyJkaXNwbGF5TmFtZSI6IkdhdHNieUpTIiwidGFnbGluZSI6IkJsYXppbmctZmFzdCBzdGF0aWMgc2l0ZSBnZW5lcmF0b3IgZm9yIFJlYWN0Iiwia2V5IjoiZ2F0c2J5anMiLCJlbnRyeXBvaW50Ijoic3JjL3BhZ2VzL2luZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJHYXRzYnlKUyAxLjkuMjQ3LCBub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiRnJhbWV3b3JrIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MtLXR1cmJpby5yZXBsLmNvL2dhdHNieWpzLnN2ZyIsInByb2plY3RfdGVtcGxhdGUiOlt7Im5hbWUiOiJnYXRzYnktYnJvd3Nlci5qcyIsImNvbnRlbnQiOiIvKipcbiAqIEltcGxlbWVudCBHYXRzYnkncyBCcm93c2VyIEFQSXMgaW4gdGhpcyBmaWxlLlxuICpcbiAqIFNlZTogaHR0cHM6Ly93d3cuZ2F0c2J5anMub3JnL2RvY3MvYnJvd3Nlci1hcGlzL1xuICovXG5cbiAvLyBZb3UgY2FuIGRlbGV0ZSB0aGlzIGZpbGUgaWYgeW91J3JlIG5vdCB1c2luZyBpdFxuIn0seyJuYW1lIjoiZ2F0c2J5LWNvbmZpZy5qcyIsImNvbnRlbnQiOiJtb2R1bGUuZXhwb3J0cyA9IHtcbiAgc2l0ZU1ldGFkYXRhOiB7XG4gICAgdGl0bGU6ICdHYXRzYnkgRGVmYXVsdCBTdGFydGVyJyxcbiAgfSxcbiAgcGx1Z2luczogWydnYXRzYnktcGx1Z2luLXJlYWN0LWhlbG1ldCddLFxufVxuIn0seyJuYW1lIjoiZ2F0c2J5LW5vZGUuanMiLCJjb250ZW50IjoiLyoqXG4gKiBJbXBsZW1lbnQgR2F0c2J5J3MgTm9kZSBBUElzIGluIHRoaXMgZmlsZS5cbiAqXG4gKiBTZWU6IGh0dHBzOi8vd3d3LmdhdHNieWpzLm9yZy9kb2NzL25vZGUtYXBpcy9cbiAqL1xuXG4gLy8gWW91IGNhbiBkZWxldGUgdGhpcyBmaWxlIGlmIHlvdSdyZSBub3QgdXNpbmcgaXRcbiJ9LHsibmFtZSI6ImdhdHNieS1zc3IuanMiLCJjb250ZW50IjoiLyoqXG4gKiBJbXBsZW1lbnQgR2F0c2J5J3MgU1NSIChTZXJ2ZXIgU2lkZSBSZW5kZXJpbmcpIEFQSXMgaW4gdGhpcyBmaWxlLlxuICpcbiAqIFNlZTogaHR0cHM6Ly93d3cuZ2F0c2J5anMub3JnL2RvY3Mvc3NyLWFwaXMvXG4gKi9cblxuIC8vIFlvdSBjYW4gZGVsZXRlIHRoaXMgZmlsZSBpZiB5b3UncmUgbm90IHVzaW5nIGl0In0seyJuYW1lIjoicGFja2FnZS5qc29uIiwiY29udGVudCI6IntcbiAgXCJuYW1lXCI6IFwibXktZ2F0c2J5LWFwcFwiLFxuICBcImRlc2NyaXB0aW9uXCI6IFwiZWFzaWx5IHRoZSBuZXh0IGluc3RhZ3JhbVwiLFxuICBcInZlcnNpb25cIjogXCIxLjAuMFwiLFxuICBcImRlcGVuZGVuY2llc1wiOiB7XG4gICAgXCJnYXRzYnlcIjogXCJeMS45LjI0N1wiLFxuICAgIFwiZ2F0c2J5LWxpbmtcIjogXCJeMS42LjQwXCIsXG4gICAgXCJnYXRzYnktcGx1Z2luLXJlYWN0LWhlbG1ldFwiOiBcIl4yLjAuMTBcIixcbiAgICBcInJlYWN0LWhlbG1ldFwiOiBcIl41LjIuMFwiXG4gIH0sXG4gIFwia2V5d29yZHNcIjogW1xuICAgIFwiZ2F0c2J5XCJcbiAgXSxcbiAgXCJsaWNlbnNlXCI6IFwiTUlUXCIsXG4gIFwic2NyaXB0c1wiOiB7XG4gICAgXCJidWlsZFwiOiBcImdhdHNieSBidWlsZFwiLFxuICAgIFwiZGV2ZWxvcFwiOiBcImdhdHNieSBkZXZlbG9wIC1IIDAuMC4wLjBcIlxuICB9XG59XG4ifSx7Im5hbWUiOiJzcmMvY29tcG9uZW50cy9oZWFkZXIuanMiLCJjb250ZW50IjoiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0J1xuaW1wb3J0IExpbmsgZnJvbSAnZ2F0c2J5LWxpbmsnXG5cbmNvbnN0IEhlYWRlciA9ICh7IHNpdGVUaXRsZSB9KSA9PiAoXG4gIDxkaXZcbiAgICBzdHlsZT17e1xuICAgICAgYmFja2dyb3VuZDogJ3JlYmVjY2FwdXJwbGUnLFxuICAgICAgbWFyZ2luQm90dG9tOiAnMS40NXJlbScsXG4gICAgfX1cbiAgPlxuICAgIDxkaXZcbiAgICAgIHN0eWxlPXt7XG4gICAgICAgIG1hcmdpbjogJzAgYXV0bycsXG4gICAgICAgIG1heFdpZHRoOiA5NjAsXG4gICAgICAgIHBhZGRpbmc6ICcxLjQ1cmVtIDEuMDg3NXJlbScsXG4gICAgICB9fVxuICAgID5cbiAgICAgIDxoMSBzdHlsZT17eyBtYXJnaW46IDAgfX0+XG4gICAgICAgIDxMaW5rXG4gICAgICAgICAgdG89XCIvXCJcbiAgICAgICAgICBzdHlsZT17e1xuICAgICAgICAgICAgY29sb3I6ICd3aGl0ZScsXG4gICAgICAgICAgICB0ZXh0RGVjb3JhdGlvbjogJ25vbmUnLFxuICAgICAgICAgIH19XG4gICAgICAgID5cbiAgICAgICAgICB7c2l0ZVRpdGxlfVxuICAgICAgICA8L0xpbms+XG4gICAgICA8L2gxPlxuICAgIDwvZGl2PlxuICA8L2Rpdj5cbilcblxuZXhwb3J0IGRlZmF1bHQgSGVhZGVyXG4ifSx7Im5hbWUiOiJzcmMvbGF5b3V0cy9pbmRleC5qcyIsImNvbnRlbnQiOiJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnXG5pbXBvcnQgUHJvcFR5cGVzIGZyb20gJ3Byb3AtdHlwZXMnXG5pbXBvcnQgSGVsbWV0IGZyb20gJ3JlYWN0LWhlbG1ldCdcblxuaW1wb3J0IEhlYWRlciBmcm9tICcuLi9jb21wb25lbnRzL2hlYWRlcidcbmltcG9ydCAnLi9pbmRleC5jc3MnXG5cbmNvbnN0IExheW91dCA9ICh7IGNoaWxkcmVuLCBkYXRhIH0pID0+IChcbiAgPGRpdj5cbiAgICA8SGVsbWV0XG4gICAgICB0aXRsZT17ZGF0YS5zaXRlLnNpdGVNZXRhZGF0YS50aXRsZX1cbiAgICAgIG1ldGE9e1tcbiAgICAgICAgeyBuYW1lOiAnZGVzY3JpcHRpb24nLCBjb250ZW50OiAnU2FtcGxlJyB9LFxuICAgICAgICB7IG5hbWU6ICdrZXl3b3JkcycsIGNvbnRlbnQ6ICdzYW1wbGUsIHNvbWV0aGluZycgfSxcbiAgICAgIF19XG4gICAgLz5cbiAgICA8SGVhZGVyIHNpdGVUaXRsZT17ZGF0YS5zaXRlLnNpdGVNZXRhZGF0YS50aXRsZX0gLz5cbiAgICA8ZGl2XG4gICAgICBzdHlsZT17e1xuICAgICAgICBtYXJnaW46ICcwIGF1dG8nLFxuICAgICAgICBtYXhXaWR0aDogOTYwLFxuICAgICAgICBwYWRkaW5nOiAnMHB4IDEuMDg3NXJlbSAxLjQ1cmVtJyxcbiAgICAgICAgcGFkZGluZ1RvcDogMCxcbiAgICAgIH19XG4gICAgPlxuICAgICAge2NoaWxkcmVuKCl9XG4gICAgPC9kaXY+XG4gIDwvZGl2PlxuKVxuXG5MYXlvdXQucHJvcFR5cGVzID0ge1xuICBjaGlsZHJlbjogUHJvcFR5cGVzLmZ1bmMsXG59XG5cbmV4cG9ydCBkZWZhdWx0IExheW91dFxuXG5leHBvcnQgY29uc3QgcXVlcnkgPSBncmFwaHFsYFxuICBxdWVyeSBTaXRlVGl0bGVRdWVyeSB7XG4gICAgc2l0ZSB7XG4gICAgICBzaXRlTWV0YWRhdGEge1xuICAgICAgICB0aXRsZVxuICAgICAgfVxuICAgIH1cbiAgfVxuYFxuIn0seyJuYW1lIjoic3JjL2xheW91dHMvaW5kZXguY3NzIiwiY29udGVudCI6Imh0bWwge1xuICBmb250LWZhbWlseTogc2Fucy1zZXJpZjtcbiAgLW1zLXRleHQtc2l6ZS1hZGp1c3Q6IDEwMCU7XG4gIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogMTAwJTtcbn1cbmJvZHkge1xuICBtYXJnaW46IDA7XG59XG5hcnRpY2xlLFxuYXNpZGUsXG5kZXRhaWxzLFxuZmlnY2FwdGlvbixcbmZpZ3VyZSxcbmZvb3RlcixcbmhlYWRlcixcbm1haW4sXG5tZW51LFxubmF2LFxuc2VjdGlvbixcbnN1bW1hcnkge1xuICBkaXNwbGF5OiBibG9jaztcbn1cbmF1ZGlvLFxuY2FudmFzLFxucHJvZ3Jlc3MsXG52aWRlbyB7XG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcbn1cbmF1ZGlvOm5vdChbY29udHJvbHNdKSB7XG4gIGRpc3BsYXk6IG5vbmU7XG4gIGhlaWdodDogMDtcbn1cbnByb2dyZXNzIHtcbiAgdmVydGljYWwtYWxpZ246IGJhc2VsaW5lO1xufVxuW2hpZGRlbl0sXG50ZW1wbGF0ZSB7XG4gIGRpc3BsYXk6IG5vbmU7XG59XG5hIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogdHJhbnNwYXJlbnQ7XG4gIC13ZWJraXQtdGV4dC1kZWNvcmF0aW9uLXNraXA6IG9iamVjdHM7XG59XG5hOmFjdGl2ZSxcbmE6aG92ZXIge1xuICBvdXRsaW5lLXdpZHRoOiAwO1xufVxuYWJiclt0aXRsZV0ge1xuICBib3JkZXItYm90dG9tOiBub25lO1xuICB0ZXh0LWRlY29yYXRpb246IHVuZGVybGluZTtcbiAgdGV4dC1kZWNvcmF0aW9uOiB1bmRlcmxpbmUgZG90dGVkO1xufVxuYixcbnN0cm9uZyB7XG4gIGZvbnQtd2VpZ2h0OiBpbmhlcml0O1xuICBmb250LXdlaWdodDogYm9sZGVyO1xufVxuZGZuIHtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuaDEge1xuICBmb250LXNpemU6IDJlbTtcbiAgbWFyZ2luOiAuNjdlbSAwO1xufVxubWFyayB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZjA7XG4gIGNvbG9yOiAjMDAwO1xufVxuc21hbGwge1xuICBmb250LXNpemU6IDgwJTtcbn1cbnN1YixcbnN1cCB7XG4gIGZvbnQtc2l6ZTogNzUlO1xuICBsaW5lLWhlaWdodDogMDtcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xuICB2ZXJ0aWNhbC1hbGlnbjogYmFzZWxpbmU7XG59XG5zdWIge1xuICBib3R0b206IC0uMjVlbTtcbn1cbnN1cCB7XG4gIHRvcDogLS41ZW07XG59XG5pbWcge1xuICBib3JkZXItc3R5bGU6IG5vbmU7XG59XG5zdmc6bm90KDpyb290KSB7XG4gIG92ZXJmbG93OiBoaWRkZW47XG59XG5jb2RlLFxua2JkLFxucHJlLFxuc2FtcCB7XG4gIGZvbnQtZmFtaWx5OiBtb25vc3BhY2UsIG1vbm9zcGFjZTtcbiAgZm9udC1zaXplOiAxZW07XG59XG5maWd1cmUge1xuICBtYXJnaW46IDFlbSA0MHB4O1xufVxuaHIge1xuICBib3gtc2l6aW5nOiBjb250ZW50LWJveDtcbiAgaGVpZ2h0OiAwO1xuICBvdmVyZmxvdzogdmlzaWJsZTtcbn1cbmJ1dHRvbixcbmlucHV0LFxub3B0Z3JvdXAsXG5zZWxlY3QsXG50ZXh0YXJlYSB7XG4gIGZvbnQ6IGluaGVyaXQ7XG4gIG1hcmdpbjogMDtcbn1cbm9wdGdyb3VwIHtcbiAgZm9udC13ZWlnaHQ6IDcwMDtcbn1cbmJ1dHRvbixcbmlucHV0IHtcbiAgb3ZlcmZsb3c6IHZpc2libGU7XG59XG5idXR0b24sXG5zZWxlY3Qge1xuICB0ZXh0LXRyYW5zZm9ybTogbm9uZTtcbn1cblt0eXBlPXJlc2V0XSxcblt0eXBlPXN1Ym1pdF0sXG5idXR0b24sXG5odG1sIFt0eXBlPWJ1dHRvbl0ge1xuICAtd2Via2l0LWFwcGVhcmFuY2U6IGJ1dHRvbjtcbn1cblt0eXBlPWJ1dHRvbl06Oi1tb3otZm9jdXMtaW5uZXIsXG5bdHlwZT1yZXNldF06Oi1tb3otZm9jdXMtaW5uZXIsXG5bdHlwZT1zdWJtaXRdOjotbW96LWZvY3VzLWlubmVyLFxuYnV0dG9uOjotbW96LWZvY3VzLWlubmVyIHtcbiAgYm9yZGVyLXN0eWxlOiBub25lO1xuICBwYWRkaW5nOiAwO1xufVxuW3R5cGU9YnV0dG9uXTotbW96LWZvY3VzcmluZyxcblt0eXBlPXJlc2V0XTotbW96LWZvY3VzcmluZyxcblt0eXBlPXN1Ym1pdF06LW1vei1mb2N1c3JpbmcsXG5idXR0b246LW1vei1mb2N1c3Jpbmcge1xuICBvdXRsaW5lOiAxcHggZG90dGVkIEJ1dHRvblRleHQ7XG59XG5maWVsZHNldCB7XG4gIGJvcmRlcjogMXB4IHNvbGlkIHNpbHZlcjtcbiAgbWFyZ2luOiAwIDJweDtcbiAgcGFkZGluZzogLjM1ZW0gLjYyNWVtIC43NWVtO1xufVxubGVnZW5kIHtcbiAgYm94LXNpemluZzogYm9yZGVyLWJveDtcbiAgY29sb3I6IGluaGVyaXQ7XG4gIGRpc3BsYXk6IHRhYmxlO1xuICBtYXgtd2lkdGg6IDEwMCU7XG4gIHBhZGRpbmc6IDA7XG4gIHdoaXRlLXNwYWNlOiBub3JtYWw7XG59XG50ZXh0YXJlYSB7XG4gIG92ZXJmbG93OiBhdXRvO1xufVxuW3R5cGU9Y2hlY2tib3hdLFxuW3R5cGU9cmFkaW9dIHtcbiAgYm94LXNpemluZzogYm9yZGVyLWJveDtcbiAgcGFkZGluZzogMDtcbn1cblt0eXBlPW51bWJlcl06Oi13ZWJraXQtaW5uZXItc3Bpbi1idXR0b24sXG5bdHlwZT1udW1iZXJdOjotd2Via2l0LW91dGVyLXNwaW4tYnV0dG9uIHtcbiAgaGVpZ2h0OiBhdXRvO1xufVxuW3R5cGU9c2VhcmNoXSB7XG4gIC13ZWJraXQtYXBwZWFyYW5jZTogdGV4dGZpZWxkO1xuICBvdXRsaW5lLW9mZnNldDogLTJweDtcbn1cblt0eXBlPXNlYXJjaF06Oi13ZWJraXQtc2VhcmNoLWNhbmNlbC1idXR0b24sXG5bdHlwZT1zZWFyY2hdOjotd2Via2l0LXNlYXJjaC1kZWNvcmF0aW9uIHtcbiAgLXdlYmtpdC1hcHBlYXJhbmNlOiBub25lO1xufVxuOjotd2Via2l0LWlucHV0LXBsYWNlaG9sZGVyIHtcbiAgY29sb3I6IGluaGVyaXQ7XG4gIG9wYWNpdHk6IC41NDtcbn1cbjo6LXdlYmtpdC1maWxlLXVwbG9hZC1idXR0b24ge1xuICAtd2Via2l0LWFwcGVhcmFuY2U6IGJ1dHRvbjtcbiAgZm9udDogaW5oZXJpdDtcbn1cbmh0bWwge1xuICBmb250OiAxMTIuNSUvMS40NWVtIGdlb3JnaWEsIHNlcmlmO1xuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICBvdmVyZmxvdy15OiBzY3JvbGw7XG59XG4qIHtcbiAgYm94LXNpemluZzogaW5oZXJpdDtcbn1cbio6YmVmb3JlIHtcbiAgYm94LXNpemluZzogaW5oZXJpdDtcbn1cbio6YWZ0ZXIge1xuICBib3gtc2l6aW5nOiBpbmhlcml0O1xufVxuYm9keSB7XG4gIGNvbG9yOiBoc2xhKDAsIDAlLCAwJSwgMC44KTtcbiAgZm9udC1mYW1pbHk6IGdlb3JnaWEsIHNlcmlmO1xuICBmb250LXdlaWdodDogbm9ybWFsO1xuICB3b3JkLXdyYXA6IGJyZWFrLXdvcmQ7XG4gIGZvbnQta2VybmluZzogbm9ybWFsO1xuICAtbW96LWZvbnQtZmVhdHVyZS1zZXR0aW5nczogXCJrZXJuXCIsIFwibGlnYVwiLCBcImNsaWdcIiwgXCJjYWx0XCI7XG4gIC1tcy1mb250LWZlYXR1cmUtc2V0dGluZ3M6IFwia2VyblwiLCBcImxpZ2FcIiwgXCJjbGlnXCIsIFwiY2FsdFwiO1xuICAtd2Via2l0LWZvbnQtZmVhdHVyZS1zZXR0aW5nczogXCJrZXJuXCIsIFwibGlnYVwiLCBcImNsaWdcIiwgXCJjYWx0XCI7XG4gIGZvbnQtZmVhdHVyZS1zZXR0aW5nczogXCJrZXJuXCIsIFwibGlnYVwiLCBcImNsaWdcIiwgXCJjYWx0XCI7XG59XG5pbWcge1xuICBtYXgtd2lkdGg6IDEwMCU7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xufVxuaDEge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbiAgY29sb3I6IGluaGVyaXQ7XG4gIGZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFNlZ29lIFVJLCBSb2JvdG8sIE94eWdlbixcbiAgICBVYnVudHUsIENhbnRhcmVsbCwgRmlyYSBTYW5zLCBEcm9pZCBTYW5zLCBIZWx2ZXRpY2EgTmV1ZSwgc2Fucy1zZXJpZjtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG4gIHRleHQtcmVuZGVyaW5nOiBvcHRpbWl6ZUxlZ2liaWxpdHk7XG4gIGZvbnQtc2l6ZTogMi4yNXJlbTtcbiAgbGluZS1oZWlnaHQ6IDEuMTtcbn1cbmgyIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG4gIGNvbG9yOiBpbmhlcml0O1xuICBmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBTZWdvZSBVSSwgUm9ib3RvLCBPeHlnZW4sXG4gICAgVWJ1bnR1LCBDYW50YXJlbGwsIEZpcmEgU2FucywgRHJvaWQgU2FucywgSGVsdmV0aWNhIE5ldWUsIHNhbnMtc2VyaWY7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xuICB0ZXh0LXJlbmRlcmluZzogb3B0aW1pemVMZWdpYmlsaXR5O1xuICBmb250LXNpemU6IDEuNjI2NzFyZW07XG4gIGxpbmUtaGVpZ2h0OiAxLjE7XG59XG5oMyB7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xuICBjb2xvcjogaW5oZXJpdDtcbiAgZm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgU2Vnb2UgVUksIFJvYm90bywgT3h5Z2VuLFxuICAgIFVidW50dSwgQ2FudGFyZWxsLCBGaXJhIFNhbnMsIERyb2lkIFNhbnMsIEhlbHZldGljYSBOZXVlLCBzYW5zLXNlcmlmO1xuICBmb250LXdlaWdodDogYm9sZDtcbiAgdGV4dC1yZW5kZXJpbmc6IG9wdGltaXplTGVnaWJpbGl0eTtcbiAgZm9udC1zaXplOiAxLjM4MzE2cmVtO1xuICBsaW5lLWhlaWdodDogMS4xO1xufVxuaDQge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbiAgY29sb3I6IGluaGVyaXQ7XG4gIGZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFNlZ29lIFVJLCBSb2JvdG8sIE94eWdlbixcbiAgICBVYnVudHUsIENhbnRhcmVsbCwgRmlyYSBTYW5zLCBEcm9pZCBTYW5zLCBIZWx2ZXRpY2EgTmV1ZSwgc2Fucy1zZXJpZjtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG4gIHRleHQtcmVuZGVyaW5nOiBvcHRpbWl6ZUxlZ2liaWxpdHk7XG4gIGZvbnQtc2l6ZTogMXJlbTtcbiAgbGluZS1oZWlnaHQ6IDEuMTtcbn1cbmg1IHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG4gIGNvbG9yOiBpbmhlcml0O1xuICBmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBTZWdvZSBVSSwgUm9ib3RvLCBPeHlnZW4sXG4gICAgVWJ1bnR1LCBDYW50YXJlbGwsIEZpcmEgU2FucywgRHJvaWQgU2FucywgSGVsdmV0aWNhIE5ldWUsIHNhbnMtc2VyaWY7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xuICB0ZXh0LXJlbmRlcmluZzogb3B0aW1pemVMZWdpYmlsaXR5O1xuICBmb250LXNpemU6IDAuODUwMjhyZW07XG4gIGxpbmUtaGVpZ2h0OiAxLjE7XG59XG5oNiB7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xuICBjb2xvcjogaW5oZXJpdDtcbiAgZm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgU2Vnb2UgVUksIFJvYm90bywgT3h5Z2VuLFxuICAgIFVidW50dSwgQ2FudGFyZWxsLCBGaXJhIFNhbnMsIERyb2lkIFNhbnMsIEhlbHZldGljYSBOZXVlLCBzYW5zLXNlcmlmO1xuICBmb250LXdlaWdodDogYm9sZDtcbiAgdGV4dC1yZW5kZXJpbmc6IG9wdGltaXplTGVnaWJpbGl0eTtcbiAgZm9udC1zaXplOiAwLjc4NDA1cmVtO1xuICBsaW5lLWhlaWdodDogMS4xO1xufVxuaGdyb3VwIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG59XG51bCB7XG4gIG1hcmdpbi1sZWZ0OiAxLjQ1cmVtO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xuICBsaXN0LXN0eWxlLXBvc2l0aW9uOiBvdXRzaWRlO1xuICBsaXN0LXN0eWxlLWltYWdlOiBub25lO1xufVxub2wge1xuICBtYXJnaW4tbGVmdDogMS40NXJlbTtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbiAgbGlzdC1zdHlsZS1wb3NpdGlvbjogb3V0c2lkZTtcbiAgbGlzdC1zdHlsZS1pbWFnZTogbm9uZTtcbn1cbmRsIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG59XG5kZCB7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xufVxucCB7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xufVxuZmlndXJlIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG59XG5wcmUge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbiAgZm9udC1zaXplOiAwLjg1cmVtO1xuICBsaW5lLWhlaWdodDogMS40MjtcbiAgYmFja2dyb3VuZDogaHNsYSgwLCAwJSwgMCUsIDAuMDQpO1xuICBib3JkZXItcmFkaXVzOiAzcHg7XG4gIG92ZXJmbG93OiBhdXRvO1xuICB3b3JkLXdyYXA6IG5vcm1hbDtcbiAgcGFkZGluZzogMS40NXJlbTtcbn1cbnRhYmxlIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG4gIGZvbnQtc2l6ZTogMXJlbTtcbiAgbGluZS1oZWlnaHQ6IDEuNDVyZW07XG4gIGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7XG4gIHdpZHRoOiAxMDAlO1xufVxuZmllbGRzZXQge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbn1cbmJsb2NrcXVvdGUge1xuICBtYXJnaW4tbGVmdDogMS40NXJlbTtcbiAgbWFyZ2luLXJpZ2h0OiAxLjQ1cmVtO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbn1cbmZvcm0ge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbn1cbm5vc2NyaXB0IHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IDEuNDVyZW07XG59XG5pZnJhbWUge1xuICBtYXJnaW4tbGVmdDogMDtcbiAgbWFyZ2luLXJpZ2h0OiAwO1xuICBtYXJnaW4tdG9wOiAwO1xuICBwYWRkaW5nLWJvdHRvbTogMDtcbiAgcGFkZGluZy1sZWZ0OiAwO1xuICBwYWRkaW5nLXJpZ2h0OiAwO1xuICBwYWRkaW5nLXRvcDogMDtcbiAgbWFyZ2luLWJvdHRvbTogMS40NXJlbTtcbn1cbmhyIHtcbiAgbWFyZ2luLWxlZnQ6IDA7XG4gIG1hcmdpbi1yaWdodDogMDtcbiAgbWFyZ2luLXRvcDogMDtcbiAgcGFkZGluZy1ib3R0b206IDA7XG4gIHBhZGRpbmctbGVmdDogMDtcbiAgcGFkZGluZy1yaWdodDogMDtcbiAgcGFkZGluZy10b3A6IDA7XG4gIG1hcmdpbi1ib3R0b206IGNhbGMoMS40NXJlbSAtIDFweCk7XG4gIGJhY2tncm91bmQ6IGhzbGEoMCwgMCUsIDAlLCAwLjIpO1xuICBib3JkZXI6IG5vbmU7XG4gIGhlaWdodDogMXB4O1xufVxuYWRkcmVzcyB7XG4gIG1hcmdpbi1sZWZ0OiAwO1xuICBtYXJnaW4tcmlnaHQ6IDA7XG4gIG1hcmdpbi10b3A6IDA7XG4gIHBhZGRpbmctYm90dG9tOiAwO1xuICBwYWRkaW5nLWxlZnQ6IDA7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG4gIHBhZGRpbmctdG9wOiAwO1xuICBtYXJnaW4tYm90dG9tOiAxLjQ1cmVtO1xufVxuYiB7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xufVxuc3Ryb25nIHtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG59XG5kdCB7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xufVxudGgge1xuICBmb250LXdlaWdodDogYm9sZDtcbn1cbmxpIHtcbiAgbWFyZ2luLWJvdHRvbTogY2FsYygxLjQ1cmVtIC8gMik7XG59XG5vbCBsaSB7XG4gIHBhZGRpbmctbGVmdDogMDtcbn1cbnVsIGxpIHtcbiAgcGFkZGluZy1sZWZ0OiAwO1xufVxubGkgPiBvbCB7XG4gIG1hcmdpbi1sZWZ0OiAxLjQ1cmVtO1xuICBtYXJnaW4tYm90dG9tOiBjYWxjKDEuNDVyZW0gLyAyKTtcbiAgbWFyZ2luLXRvcDogY2FsYygxLjQ1cmVtIC8gMik7XG59XG5saSA+IHVsIHtcbiAgbWFyZ2luLWxlZnQ6IDEuNDVyZW07XG4gIG1hcmdpbi1ib3R0b206IGNhbGMoMS40NXJlbSAvIDIpO1xuICBtYXJnaW4tdG9wOiBjYWxjKDEuNDVyZW0gLyAyKTtcbn1cbmJsb2NrcXVvdGUgKjpsYXN0LWNoaWxkIHtcbiAgbWFyZ2luLWJvdHRvbTogMDtcbn1cbmxpICo6bGFzdC1jaGlsZCB7XG4gIG1hcmdpbi1ib3R0b206IDA7XG59XG5wICo6bGFzdC1jaGlsZCB7XG4gIG1hcmdpbi1ib3R0b206IDA7XG59XG5saSA+IHAge1xuICBtYXJnaW4tYm90dG9tOiBjYWxjKDEuNDVyZW0gLyAyKTtcbn1cbmNvZGUge1xuICBmb250LXNpemU6IDAuODVyZW07XG4gIGxpbmUtaGVpZ2h0OiAxLjQ1cmVtO1xufVxua2JkIHtcbiAgZm9udC1zaXplOiAwLjg1cmVtO1xuICBsaW5lLWhlaWdodDogMS40NXJlbTtcbn1cbnNhbXAge1xuICBmb250LXNpemU6IDAuODVyZW07XG4gIGxpbmUtaGVpZ2h0OiAxLjQ1cmVtO1xufVxuYWJiciB7XG4gIGJvcmRlci1ib3R0b206IDFweCBkb3R0ZWQgaHNsYSgwLCAwJSwgMCUsIDAuNSk7XG4gIGN1cnNvcjogaGVscDtcbn1cbmFjcm9ueW0ge1xuICBib3JkZXItYm90dG9tOiAxcHggZG90dGVkIGhzbGEoMCwgMCUsIDAlLCAwLjUpO1xuICBjdXJzb3I6IGhlbHA7XG59XG5hYmJyW3RpdGxlXSB7XG4gIGJvcmRlci1ib3R0b206IDFweCBkb3R0ZWQgaHNsYSgwLCAwJSwgMCUsIDAuNSk7XG4gIGN1cnNvcjogaGVscDtcbiAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xufVxudGhlYWQge1xuICB0ZXh0LWFsaWduOiBsZWZ0O1xufVxudGQsXG50aCB7XG4gIHRleHQtYWxpZ246IGxlZnQ7XG4gIGJvcmRlci1ib3R0b206IDFweCBzb2xpZCBoc2xhKDAsIDAlLCAwJSwgMC4xMik7XG4gIGZvbnQtZmVhdHVyZS1zZXR0aW5nczogXCJ0bnVtXCI7XG4gIC1tb3otZm9udC1mZWF0dXJlLXNldHRpbmdzOiBcInRudW1cIjtcbiAgLW1zLWZvbnQtZmVhdHVyZS1zZXR0aW5nczogXCJ0bnVtXCI7XG4gIC13ZWJraXQtZm9udC1mZWF0dXJlLXNldHRpbmdzOiBcInRudW1cIjtcbiAgcGFkZGluZy1sZWZ0OiAwLjk2NjY3cmVtO1xuICBwYWRkaW5nLXJpZ2h0OiAwLjk2NjY3cmVtO1xuICBwYWRkaW5nLXRvcDogMC43MjVyZW07XG4gIHBhZGRpbmctYm90dG9tOiBjYWxjKDAuNzI1cmVtIC0gMXB4KTtcbn1cbnRoOmZpcnN0LWNoaWxkLFxudGQ6Zmlyc3QtY2hpbGQge1xuICBwYWRkaW5nLWxlZnQ6IDA7XG59XG50aDpsYXN0LWNoaWxkLFxudGQ6bGFzdC1jaGlsZCB7XG4gIHBhZGRpbmctcmlnaHQ6IDA7XG59XG50dCxcbmNvZGUge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiBoc2xhKDAsIDAlLCAwJSwgMC4wNCk7XG4gIGJvcmRlci1yYWRpdXM6IDNweDtcbiAgZm9udC1mYW1pbHk6IFwiU0ZNb25vLVJlZ3VsYXJcIiwgQ29uc29sYXMsIFwiUm9ib3RvIE1vbm9cIiwgXCJEcm9pZCBTYW5zIE1vbm9cIixcbiAgICBcIkxpYmVyYXRpb24gTW9ub1wiLCBNZW5sbywgQ291cmllciwgbW9ub3NwYWNlO1xuICBwYWRkaW5nOiAwO1xuICBwYWRkaW5nLXRvcDogMC4yZW07XG4gIHBhZGRpbmctYm90dG9tOiAwLjJlbTtcbn1cbnByZSBjb2RlIHtcbiAgYmFja2dyb3VuZDogbm9uZTtcbiAgbGluZS1oZWlnaHQ6IDEuNDI7XG59XG5jb2RlOmJlZm9yZSxcbmNvZGU6YWZ0ZXIsXG50dDpiZWZvcmUsXG50dDphZnRlciB7XG4gIGxldHRlci1zcGFjaW5nOiAtMC4yZW07XG4gIGNvbnRlbnQ6IFwiIFwiO1xufVxucHJlIGNvZGU6YmVmb3JlLFxucHJlIGNvZGU6YWZ0ZXIsXG5wcmUgdHQ6YmVmb3JlLFxucHJlIHR0OmFmdGVyIHtcbiAgY29udGVudDogXCJcIjtcbn1cbkBtZWRpYSBvbmx5IHNjcmVlbiBhbmQgKG1heC13aWR0aDogNDgwcHgpIHtcbiAgaHRtbCB7XG4gICAgZm9udC1zaXplOiAxMDAlO1xuICB9XG59XG4ifSx7Im5hbWUiOiJzcmMvcGFnZXMvaW5kZXguanMiLCJjb250ZW50IjoiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0J1xuaW1wb3J0IExpbmsgZnJvbSAnZ2F0c2J5LWxpbmsnXG5cbmNvbnN0IEluZGV4UGFnZSA9ICgpID0+IChcbiAgPGRpdj5cbiAgICA8aDE+SGkgcGVvcGxlPC9oMT5cbiAgICA8cD5XZWxjb21lIHRvIHlvdXIgbmV3IEdhdHNieSBzaXRlLjwvcD5cbiAgICA8cD5Ob3cgZ28gYnVpbGQgc29tZXRoaW5nIGdyZWF0LjwvcD5cbiAgICA8TGluayB0bz1cIi9wYWdlLTIvXCI+R28gdG8gcGFnZSAyPC9MaW5rPlxuICA8L2Rpdj5cbilcblxuZXhwb3J0IGRlZmF1bHQgSW5kZXhQYWdlXG4ifSx7Im5hbWUiOiJzcmMvcGFnZXMvNDA0LmpzIiwiY29udGVudCI6ImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCdcblxuY29uc3QgTm90Rm91bmRQYWdlID0gKCkgPT4gKFxuICA8ZGl2PlxuICAgIDxoMT5OT1QgRk9VTkQ8L2gxPlxuICAgIDxwPllvdSBqdXN0IGhpdCBhIHJvdXRlIHRoYXQgZG9lc24mIzM5O3QgZXhpc3QuLi4gdGhlIHNhZG5lc3MuPC9wPlxuICA8L2Rpdj5cbilcblxuZXhwb3J0IGRlZmF1bHQgTm90Rm91bmRQYWdlXG4ifSx7Im5hbWUiOiJzcmMvcGFnZXMvcGFnZS0yLmpzIiwiY29udGVudCI6ImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCdcbmltcG9ydCBMaW5rIGZyb20gJ2dhdHNieS1saW5rJ1xuXG5jb25zdCBTZWNvbmRQYWdlID0gKCkgPT4gKFxuICA8ZGl2PlxuICAgIDxoMT5IaSBmcm9tIHRoZSBzZWNvbmQgcGFnZTwvaDE+XG4gICAgPHA+V2VsY29tZSB0byBwYWdlIDI8L3A+XG4gICAgPExpbmsgdG89XCIvXCI+R28gYmFjayB0byB0aGUgaG9tZXBhZ2U8L0xpbms+XG4gIDwvZGl2PlxuKVxuXG5leHBvcnQgZGVmYXVsdCBTZWNvbmRQYWdlXG4ifV0sIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwiLCJjb25maWciOnsiaXNTZXJ2ZXIiOnRydWV9fSwicmVhY3RqcyI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IiwidGFnbGluZSI6IkEgSmF2YVNjcmlwdCBsaWJyYXJ5IGZvciBidWlsZGluZyB1c2VyIGludGVyZmFjZXMiLCJrZXkiOiJyZWFjdGpzIiwiZW50cnlwb2ludCI6InNyYy9pbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoiUmVhY3QgMTYuNC4wLCBub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiRnJhbWV3b3JrIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MtLXR1cmJpby5yZXBsLmNvL3JlYWN0anMuc3ZnIiwicHJvamVjdF90ZW1wbGF0ZSI6W3sibmFtZSI6InBhY2thZ2UuanNvbiIsImNvbnRlbnQiOiJ7XG4gIFwibmFtZVwiOiBcInJ1bm5lclwiLFxuICBcInZlcnNpb25cIjogXCIwLjEuMFwiLFxuICBcInByaXZhdGVcIjogdHJ1ZSxcbiAgXCJkZXBlbmRlbmNpZXNcIjoge1xuICAgIFwicmVhY3RcIjogXCJeMTYuNC4wXCIsXG4gICAgXCJyZWFjdC1kb21cIjogXCJeMTYuNC4wXCIsXG4gICAgXCJyZWFjdC1zY3JpcHRzXCI6IFwiMS4xLjRcIlxuICB9LFxuICBcInNjcmlwdHNcIjoge1xuICAgIFwic3RhcnRcIjogXCJyZWFjdC1zY3JpcHRzIHN0YXJ0XCIsXG4gICAgXCJidWlsZFwiOiBcInJlYWN0LXNjcmlwdHMgYnVpbGRcIixcbiAgICBcInRlc3RcIjogXCJyZWFjdC1zY3JpcHRzIHRlc3QgLS1lbnY9anNkb21cIixcbiAgICBcImVqZWN0XCI6IFwicmVhY3Qtc2NyaXB0cyBlamVjdFwiXG4gIH1cbn0ifSx7Im5hbWUiOiJzcmMvaW5kZXguY3NzIiwiY29udGVudCI6ImJvZHkge1xuICBtYXJnaW46IDA7XG4gIHBhZGRpbmc6IDA7XG4gIGZvbnQtZmFtaWx5OiBzYW5zLXNlcmlmO1xufVxuIn0seyJuYW1lIjoic3JjL2luZGV4LmpzIiwiY29udGVudCI6ImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgUmVhY3RET00gZnJvbSAncmVhY3QtZG9tJztcbmltcG9ydCAnLi9pbmRleC5jc3MnO1xuaW1wb3J0IEFwcCBmcm9tICcuL0FwcCc7XG5cblJlYWN0RE9NLnJlbmRlcig8QXBwIC8+LCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgncm9vdCcpKTsifSx7Im5hbWUiOiJzcmMvQXBwLmNzcyIsImNvbnRlbnQiOiIuQXBwIHtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xufVxuXG4uQXBwLWxvZ28ge1xuICBhbmltYXRpb246IEFwcC1sb2dvLXNwaW4gaW5maW5pdGUgMjBzIGxpbmVhcjtcbiAgaGVpZ2h0OiA4MHB4O1xufVxuXG4uQXBwLWhlYWRlciB7XG4gIGJhY2tncm91bmQtY29sb3I6ICMyMjI7XG4gIGhlaWdodDogMTUwcHg7XG4gIHBhZGRpbmc6IDIwcHg7XG4gIGNvbG9yOiB3aGl0ZTtcbn1cblxuLkFwcC10aXRsZSB7XG4gIGZvbnQtc2l6ZTogMS41ZW07XG59XG5cbi5BcHAtaW50cm8ge1xuICBmb250LXNpemU6IGxhcmdlO1xufVxuXG5Aa2V5ZnJhbWVzIEFwcC1sb2dvLXNwaW4ge1xuICBmcm9tIHsgdHJhbnNmb3JtOiByb3RhdGUoMGRlZyk7IH1cbiAgdG8geyB0cmFuc2Zvcm06IHJvdGF0ZSgzNjBkZWcpOyB9XG59XG4ifSx7Im5hbWUiOiJzcmMvbG9nby5zdmciLCJjb250ZW50IjoiPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgdmlld0JveD1cIjAgMCA4NDEuOSA1OTUuM1wiPlxuICAgIDxnIGZpbGw9XCIjNjFEQUZCXCI+XG4gICAgICAgIDxwYXRoIGQ9XCJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40elwiLz5cbiAgICAgICAgPGNpcmNsZSBjeD1cIjQyMC45XCIgY3k9XCIyOTYuNVwiIHI9XCI0NS43XCIvPlxuICAgICAgICA8cGF0aCBkPVwiTTUyMC41IDc4LjF6XCIvPlxuICAgIDwvZz5cbjwvc3ZnPlxuIn0seyJuYW1lIjoic3JjL0FwcC5qcyIsImNvbnRlbnQiOiJpbXBvcnQgUmVhY3QsIHsgQ29tcG9uZW50IH0gZnJvbSAncmVhY3QnO1xuaW1wb3J0IGxvZ28gZnJvbSAnLi9sb2dvLnN2Zyc7XG5pbXBvcnQgJy4vQXBwLmNzcyc7XG5cbmNsYXNzIEFwcCBleHRlbmRzIENvbXBvbmVudCB7XG4gIHJlbmRlcigpIHtcbiAgICByZXR1cm4gKFxuICAgICAgPGRpdiBjbGFzc05hbWU9XCJBcHBcIj5cbiAgICAgICAgPGhlYWRlciBjbGFzc05hbWU9XCJBcHAtaGVhZGVyXCI+XG4gICAgICAgICAgPGltZyBzcmM9e2xvZ299IGNsYXNzTmFtZT1cIkFwcC1sb2dvXCIgYWx0PVwibG9nb1wiIC8+XG4gICAgICAgICAgPGgxIGNsYXNzTmFtZT1cIkFwcC10aXRsZVwiPldlbGNvbWUgdG8gUmVhY3Q8L2gxPlxuICAgICAgICA8L2hlYWRlcj5cbiAgICAgICAgPHAgY2xhc3NOYW1lPVwiQXBwLWludHJvXCI+XG4gICAgICAgICAgVG8gZ2V0IHN0YXJ0ZWQsIGVkaXQgPGNvZGU+c3JjL0FwcC5qczwvY29kZT4gYW5kIHNhdmUgdG8gcmVsb2FkLlxuICAgICAgICA8L3A+XG4gICAgICA8L2Rpdj5cbiAgICApO1xuICB9XG59XG5cbmV4cG9ydCBkZWZhdWx0IEFwcDtcbiJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJyZWFjdHRzIjp7ImRpc3BsYXlOYW1lIjoiUmVhY3QgVHlwZXNjcmlwdCIsInRhZ2xpbmUiOiJBIEphdmFTY3JpcHQgbGlicmFyeSBmb3IgYnVpbGRpbmcgdXNlciBpbnRlcmZhY2VzIiwia2V5IjoicmVhY3R0cyIsImVudHJ5cG9pbnQiOiJzcmMvaW5kZXgudHN4IiwiZXh0IjoidHN4IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoiUmVhY3QgMTYuNC4wLCBub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiRnJhbWV3b3JrIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MtLXR1cmJpby5yZXBsLmNvL3JlYWN0dHMuc3ZnIiwicHJvamVjdF90ZW1wbGF0ZSI6W3sibmFtZSI6InBhY2thZ2UuanNvbiIsImNvbnRlbnQiOiJ7XG4gIFwibmFtZVwiOiBcInJ1bm5lclwiLFxuICBcInZlcnNpb25cIjogXCIwLjEuMFwiLFxuICBcInByaXZhdGVcIjogdHJ1ZSxcbiAgXCJkZXBlbmRlbmNpZXNcIjoge1xuICAgIFwicmVhY3RcIjogXCJeMTYuNC4wXCIsXG4gICAgXCJyZWFjdC1kb21cIjogXCJeMTYuNC4wXCIsXG4gICAgXCJyZWFjdC1zY3JpcHRzLXRzXCI6IFwiMi4xNi4wXCJcbiAgfSxcbiAgXCJzY3JpcHRzXCI6IHtcbiAgICBcInN0YXJ0XCI6IFwicmVhY3Qtc2NyaXB0cy10cyBzdGFydFwiLFxuICAgIFwiYnVpbGRcIjogXCJyZWFjdC1zY3JpcHRzLXRzIGJ1aWxkXCIsXG4gICAgXCJ0ZXN0XCI6IFwicmVhY3Qtc2NyaXB0cy10cyB0ZXN0IC0tZW52PWpzZG9tXCIsXG4gICAgXCJlamVjdFwiOiBcInJlYWN0LXNjcmlwdHMtdHMgZWplY3RcIlxuICB9LFxuICBcImRldkRlcGVuZGVuY2llc1wiOiB7XG4gICAgXCJAdHlwZXMvamVzdFwiOiBcIl4yMy4wLjBcIixcbiAgICBcIkB0eXBlcy9ub2RlXCI6IFwiXjEwLjMuMVwiLFxuICAgIFwiQHR5cGVzL3JlYWN0XCI6IFwiXjE2LjMuMTZcIixcbiAgICBcIkB0eXBlcy9yZWFjdC1kb21cIjogXCJeMTYuMC42XCIsXG4gICAgXCJ0eXBlc2NyaXB0XCI6IFwiXjIuOS4xXCJcbiAgfVxufVxuIn0seyJuYW1lIjoiaW1hZ2VzLmQudHMiLCJjb250ZW50IjoiZGVjbGFyZSBtb2R1bGUgJyouc3ZnJ1xuZGVjbGFyZSBtb2R1bGUgJyoucG5nJ1xuZGVjbGFyZSBtb2R1bGUgJyouanBnJ1xuIn0seyJuYW1lIjoic3JjL2luZGV4LmNzcyIsImNvbnRlbnQiOiJib2R5IHtcbiAgbWFyZ2luOiAwO1xuICBwYWRkaW5nOiAwO1xuICBmb250LWZhbWlseTogc2Fucy1zZXJpZjtcbn1cbiJ9LHsibmFtZSI6InNyYy9BcHAuY3NzIiwiY29udGVudCI6Ii5BcHAge1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG59XG5cbi5BcHAtbG9nbyB7XG4gIGFuaW1hdGlvbjogQXBwLWxvZ28tc3BpbiBpbmZpbml0ZSAyMHMgbGluZWFyO1xuICBoZWlnaHQ6IDgwcHg7XG59XG5cbi5BcHAtaGVhZGVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzIyMjtcbiAgaGVpZ2h0OiAxNTBweDtcbiAgcGFkZGluZzogMjBweDtcbiAgY29sb3I6IHdoaXRlO1xufVxuXG4uQXBwLXRpdGxlIHtcbiAgZm9udC1zaXplOiAxLjVlbTtcbn1cblxuLkFwcC1pbnRybyB7XG4gIGZvbnQtc2l6ZTogbGFyZ2U7XG59XG5cbkBrZXlmcmFtZXMgQXBwLWxvZ28tc3BpbiB7XG4gIGZyb20geyB0cmFuc2Zvcm06IHJvdGF0ZSgwZGVnKTsgfVxuICB0byB7IHRyYW5zZm9ybTogcm90YXRlKDM2MGRlZyk7IH1cbn1cbiJ9LHsibmFtZSI6InNyYy9pbmRleC50c3giLCJjb250ZW50IjoiaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0ICogYXMgUmVhY3RET00gZnJvbSAncmVhY3QtZG9tJztcbmltcG9ydCBBcHAgZnJvbSAnLi9BcHAnO1xuaW1wb3J0ICcuL2luZGV4LmNzcyc7XG5cblJlYWN0RE9NLnJlbmRlcihcbiAgPEFwcCAvPixcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3Jvb3QnKSBhcyBIVE1MRWxlbWVudFxuKTtcbiJ9LHsibmFtZSI6InNyYy9sb2dvLnN2ZyIsImNvbnRlbnQiOiI8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiB2aWV3Qm94PVwiMCAwIDg0MS45IDU5NS4zXCI+XG4gICAgPGcgZmlsbD1cIiM2MURBRkJcIj5cbiAgICAgICAgPHBhdGggZD1cIk02NjYuMyAyOTYuNWMwLTMyLjUtNDAuNy02My4zLTEwMy4xLTgyLjQgMTQuNC02My42IDgtMTE0LjItMjAuMi0xMzAuNC02LjUtMy44LTE0LjEtNS42LTIyLjQtNS42djIyLjNjNC42IDAgOC4zLjkgMTEuNCAyLjYgMTMuNiA3LjggMTkuNSAzNy41IDE0LjkgNzUuNy0xLjEgOS40LTIuOSAxOS4zLTUuMSAyOS40LTE5LjYtNC44LTQxLTguNS02My41LTEwLjktMTMuNS0xOC41LTI3LjUtMzUuMy00MS42LTUwIDMyLjYtMzAuMyA2My4yLTQ2LjkgODQtNDYuOVY3OGMtMjcuNSAwLTYzLjUgMTkuNi05OS45IDUzLjYtMzYuNC0zMy44LTcyLjQtNTMuMi05OS45LTUzLjJ2MjIuM2MyMC43IDAgNTEuNCAxNi41IDg0IDQ2LjYtMTQgMTQuNy0yOCAzMS40LTQxLjMgNDkuOS0yMi42IDIuNC00NCA2LjEtNjMuNiAxMS0yLjMtMTAtNC0xOS43LTUuMi0yOS00LjctMzguMiAxLjEtNjcuOSAxNC42LTc1LjggMy0xLjggNi45LTIuNiAxMS41LTIuNlY3OC41Yy04LjQgMC0xNiAxLjgtMjIuNiA1LjYtMjguMSAxNi4yLTM0LjQgNjYuNy0xOS45IDEzMC4xLTYyLjIgMTkuMi0xMDIuNyA0OS45LTEwMi43IDgyLjMgMCAzMi41IDQwLjcgNjMuMyAxMDMuMSA4Mi40LTE0LjQgNjMuNi04IDExNC4yIDIwLjIgMTMwLjQgNi41IDMuOCAxNC4xIDUuNiAyMi41IDUuNiAyNy41IDAgNjMuNS0xOS42IDk5LjktNTMuNiAzNi40IDMzLjggNzIuNCA1My4yIDk5LjkgNTMuMiA4LjQgMCAxNi0xLjggMjIuNi01LjYgMjguMS0xNi4yIDM0LjQtNjYuNyAxOS45LTEzMC4xIDYyLTE5LjEgMTAyLjUtNDkuOSAxMDIuNS04Mi4zem0tMTMwLjItNjYuN2MtMy43IDEyLjktOC4zIDI2LjItMTMuNSAzOS41LTQuMS04LTguNC0xNi0xMy4xLTI0LTQuNi04LTkuNS0xNS44LTE0LjQtMjMuNCAxNC4yIDIuMSAyNy45IDQuNyA0MSA3Ljl6bS00NS44IDEwNi41Yy03LjggMTMuNS0xNS44IDI2LjMtMjQuMSAzOC4yLTE0LjkgMS4zLTMwIDItNDUuMiAyLTE1LjEgMC0zMC4yLS43LTQ1LTEuOS04LjMtMTEuOS0xNi40LTI0LjYtMjQuMi0zOC03LjYtMTMuMS0xNC41LTI2LjQtMjAuOC0zOS44IDYuMi0xMy40IDEzLjItMjYuOCAyMC43LTM5LjkgNy44LTEzLjUgMTUuOC0yNi4zIDI0LjEtMzguMiAxNC45LTEuMyAzMC0yIDQ1LjItMiAxNS4xIDAgMzAuMi43IDQ1IDEuOSA4LjMgMTEuOSAxNi40IDI0LjYgMjQuMiAzOCA3LjYgMTMuMSAxNC41IDI2LjQgMjAuOCAzOS44LTYuMyAxMy40LTEzLjIgMjYuOC0yMC43IDM5Ljl6bTMyLjMtMTNjNS40IDEzLjQgMTAgMjYuOCAxMy44IDM5LjgtMTMuMSAzLjItMjYuOSA1LjktNDEuMiA4IDQuOS03LjcgOS44LTE1LjYgMTQuNC0yMy43IDQuNi04IDguOS0xNi4xIDEzLTI0LjF6TTQyMS4yIDQzMGMtOS4zLTkuNi0xOC42LTIwLjMtMjcuOC0zMiA5IC40IDE4LjIuNyAyNy41LjcgOS40IDAgMTguNy0uMiAyNy44LS43LTkgMTEuNy0xOC4zIDIyLjQtMjcuNSAzMnptLTc0LjQtNTguOWMtMTQuMi0yLjEtMjcuOS00LjctNDEtNy45IDMuNy0xMi45IDguMy0yNi4yIDEzLjUtMzkuNSA0LjEgOCA4LjQgMTYgMTMuMSAyNCA0LjcgOCA5LjUgMTUuOCAxNC40IDIzLjR6TTQyMC43IDE2M2M5LjMgOS42IDE4LjYgMjAuMyAyNy44IDMyLTktLjQtMTguMi0uNy0yNy41LS43LTkuNCAwLTE4LjcuMi0yNy44LjcgOS0xMS43IDE4LjMtMjIuNCAyNy41LTMyem0tNzQgNTguOWMtNC45IDcuNy05LjggMTUuNi0xNC40IDIzLjctNC42IDgtOC45IDE2LTEzIDI0LTUuNC0xMy40LTEwLTI2LjgtMTMuOC0zOS44IDEzLjEtMy4xIDI2LjktNS44IDQxLjItNy45em0tOTAuNSAxMjUuMmMtMzUuNC0xNS4xLTU4LjMtMzQuOS01OC4zLTUwLjYgMC0xNS43IDIyLjktMzUuNiA1OC4zLTUwLjYgOC42LTMuNyAxOC03IDI3LjctMTAuMSA1LjcgMTkuNiAxMy4yIDQwIDIyLjUgNjAuOS05LjIgMjAuOC0xNi42IDQxLjEtMjIuMiA2MC42LTkuOS0zLjEtMTkuMy02LjUtMjgtMTAuMnpNMzEwIDQ5MGMtMTMuNi03LjgtMTkuNS0zNy41LTE0LjktNzUuNyAxLjEtOS40IDIuOS0xOS4zIDUuMS0yOS40IDE5LjYgNC44IDQxIDguNSA2My41IDEwLjkgMTMuNSAxOC41IDI3LjUgMzUuMyA0MS42IDUwLTMyLjYgMzAuMy02My4yIDQ2LjktODQgNDYuOS00LjUtLjEtOC4zLTEtMTEuMy0yLjd6bTIzNy4yLTc2LjJjNC43IDM4LjItMS4xIDY3LjktMTQuNiA3NS44LTMgMS44LTYuOSAyLjYtMTEuNSAyLjYtMjAuNyAwLTUxLjQtMTYuNS04NC00Ni42IDE0LTE0LjcgMjgtMzEuNCA0MS4zLTQ5LjkgMjIuNi0yLjQgNDQtNi4xIDYzLjYtMTEgMi4zIDEwLjEgNC4xIDE5LjggNS4yIDI5LjF6bTM4LjUtNjYuN2MtOC42IDMuNy0xOCA3LTI3LjcgMTAuMS01LjctMTkuNi0xMy4yLTQwLTIyLjUtNjAuOSA5LjItMjAuOCAxNi42LTQxLjEgMjIuMi02MC42IDkuOSAzLjEgMTkuMyA2LjUgMjguMSAxMC4yIDM1LjQgMTUuMSA1OC4zIDM0LjkgNTguMyA1MC42LS4xIDE1LjctMjMgMzUuNi01OC40IDUwLjZ6TTMyMC44IDc4LjR6XCIvPlxuICAgICAgICA8Y2lyY2xlIGN4PVwiNDIwLjlcIiBjeT1cIjI5Ni41XCIgcj1cIjQ1LjdcIi8+XG4gICAgICAgIDxwYXRoIGQ9XCJNNTIwLjUgNzguMXpcIi8+XG4gICAgPC9nPlxuPC9zdmc+XG4ifSx7Im5hbWUiOiJzcmMvQXBwLnRzeCIsImNvbnRlbnQiOiJpbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgJy4vQXBwLmNzcyc7XG5cbmltcG9ydCBsb2dvIGZyb20gJy4vbG9nby5zdmcnO1xuXG5jbGFzcyBBcHAgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQge1xuICBwdWJsaWMgcmVuZGVyKCkge1xuICAgIHJldHVybiAoXG4gICAgICA8ZGl2IGNsYXNzTmFtZT1cIkFwcFwiPlxuICAgICAgICA8aGVhZGVyIGNsYXNzTmFtZT1cIkFwcC1oZWFkZXJcIj5cbiAgICAgICAgICA8aW1nIHNyYz17bG9nb30gY2xhc3NOYW1lPVwiQXBwLWxvZ29cIiBhbHQ9XCJsb2dvXCIgLz5cbiAgICAgICAgICA8aDEgY2xhc3NOYW1lPVwiQXBwLXRpdGxlXCI+V2VsY29tZSB0byBSZWFjdDwvaDE+XG4gICAgICAgIDwvaGVhZGVyPlxuICAgICAgICA8cCBjbGFzc05hbWU9XCJBcHAtaW50cm9cIj5cbiAgICAgICAgICBUbyBnZXQgc3RhcnRlZCwgZWRpdCA8Y29kZT5zcmMvQXBwLnRzeDwvY29kZT4gYW5kIHNhdmUgdG8gcmVsb2FkLlxuICAgICAgICA8L3A+XG4gICAgICA8L2Rpdj5cbiAgICApO1xuICB9XG59XG5cbmV4cG9ydCBkZWZhdWx0IEFwcDtcbiJ9LHsibmFtZSI6InRzY29uZmlnLmpzb24iLCJjb250ZW50Ijoie1xuICBcImNvbXBpbGVyT3B0aW9uc1wiOiB7XG4gICAgXCJiYXNlVXJsXCI6IFwiLlwiLFxuICAgIFwib3V0RGlyXCI6IFwiYnVpbGQvZGlzdFwiLFxuICAgIFwibW9kdWxlXCI6IFwiZXNuZXh0XCIsXG4gICAgXCJ0YXJnZXRcIjogXCJlczVcIixcbiAgICBcImxpYlwiOiBbXCJlczZcIiwgXCJkb21cIl0sXG4gICAgXCJzb3VyY2VNYXBcIjogdHJ1ZSxcbiAgICBcImFsbG93SnNcIjogdHJ1ZSxcbiAgICBcImpzeFwiOiBcInJlYWN0XCIsXG4gICAgXCJtb2R1bGVSZXNvbHV0aW9uXCI6IFwibm9kZVwiLFxuICAgIFwicm9vdERpclwiOiBcInNyY1wiLFxuICAgIFwiZm9yY2VDb25zaXN0ZW50Q2FzaW5nSW5GaWxlTmFtZXNcIjogdHJ1ZSxcbiAgICBcIm5vSW1wbGljaXRSZXR1cm5zXCI6IHRydWUsXG4gICAgXCJub0ltcGxpY2l0VGhpc1wiOiB0cnVlLFxuICAgIFwibm9JbXBsaWNpdEFueVwiOiB0cnVlLFxuICAgIFwic3RyaWN0TnVsbENoZWNrc1wiOiB0cnVlLFxuICAgIFwic3VwcHJlc3NJbXBsaWNpdEFueUluZGV4RXJyb3JzXCI6IHRydWUsXG4gICAgXCJub1VudXNlZExvY2Fsc1wiOiB0cnVlXG4gIH0sXG4gIFwiZXhjbHVkZVwiOiBbXG4gICAgXCJub2RlX21vZHVsZXNcIixcbiAgICBcImJ1aWxkXCIsXG4gICAgXCJzY3JpcHRzXCIsXG4gICAgXCJhY2NlcHRhbmNlLXRlc3RzXCIsXG4gICAgXCJ3ZWJwYWNrXCIsXG4gICAgXCJqZXN0XCIsXG4gICAgXCJzcmMvc2V0dXBUZXN0cy50c1wiXG4gIF1cbn1cbiJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJyZWFjdHJlIjp7ImRpc3BsYXlOYW1lIjoiUmVhY3QgUmVhc29uIiwidGFnbGluZSI6IlJlYXNvbiBiaW5kaW5ncyBmb3IgUmVhY3RKUyIsImtleSI6InJlYWN0cmUiLCJlbnRyeXBvaW50Ijoic3JjL2luZGV4LnJlIiwiZXh0IjoicmUiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoZWFkZXIiOiJSZWFzb24gMy4xLjUsIG5vZGUgdjkuNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJGcmFtZXdvcmsiLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy0tdHVyYmlvLnJlcGwuY28vcmVhY3RyZS5zdmciLCJwcm9qZWN0X3RlbXBsYXRlIjpbeyJuYW1lIjoicGFja2FnZS5qc29uIiwiY29udGVudCI6IntcbiAgXCJuYW1lXCI6IFwiYXBwXCIsXG4gIFwidmVyc2lvblwiOiBcIjAuMS4wXCIsXG4gIFwicHJpdmF0ZVwiOiB0cnVlLFxuICBcImRlcGVuZGVuY2llc1wiOiB7XG4gICAgXCJyZWFjdFwiOiBcIl4xNi40LjBcIixcbiAgICBcInJlYWN0LWRvbVwiOiBcIl4xNi40LjBcIixcbiAgICBcInJlYXNvbi1zY3JpcHRzXCI6IFwiMC45LjBcIlxuICB9LFxuICBcInNjcmlwdHNcIjoge1xuICAgIFwic3RhcnRcIjogXCJyZWFjdC1zY3JpcHRzIHN0YXJ0XCIsXG4gICAgXCJidWlsZFwiOiBcInJlYWN0LXNjcmlwdHMgYnVpbGRcIixcbiAgICBcInRlc3RcIjogXCJyZWFjdC1zY3JpcHRzIHRlc3QgLS1lbnY9anNkb21cIixcbiAgICBcImVqZWN0XCI6IFwicmVhY3Qtc2NyaXB0cyBlamVjdFwiXG4gIH0sXG4gIFwiZGV2RGVwZW5kZW5jaWVzXCI6IHtcbiAgICBcIkBnbGVubnNsL2JzLWplc3RcIjogXCJeMC40LjJcIixcbiAgICBcInJlYXNvbi1yZWFjdFwiOiBcIl4wLjQuMlwiXG4gIH1cbn1cbiJ9LHsibmFtZSI6InNyYy9pbmRleC5yZSIsImNvbnRlbnQiOiJbJWJzLnJhdyB7fHJlcXVpcmUoJy4vaW5kZXguY3NzJyl8fV07XG5cblJlYWN0RE9NUmUucmVuZGVyVG9FbGVtZW50V2l0aElkKFxuICA8QXBwIG1lc3NhZ2U9XCJXZWxjb21lIHRvIFJlYWN0IGFuZCBSZWFzb25cIiAvPixcbiAgXCJyb290XCIsXG4pOyJ9LHsibmFtZSI6InNyYy9pbmRleC5jc3MiLCJjb250ZW50IjoiYm9keSB7XG4gIG1hcmdpbjogMDtcbiAgcGFkZGluZzogMDtcbiAgZm9udC1mYW1pbHk6IHNhbnMtc2VyaWY7XG59XG4ifSx7Im5hbWUiOiJzcmMvQXBwLmNzcyIsImNvbnRlbnQiOiIuQXBwIHtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xufVxuXG4uQXBwLWxvZ28ge1xuICBhbmltYXRpb246IEFwcC1sb2dvLXNwaW4gaW5maW5pdGUgMjBzIGxpbmVhcjtcbiAgaGVpZ2h0OiA4MHB4O1xufVxuXG4uQXBwLWhlYWRlciB7XG4gIGJhY2tncm91bmQtY29sb3I6ICMyMjI7XG4gIGhlaWdodDogMTUwcHg7XG4gIHBhZGRpbmc6IDIwcHg7XG4gIGNvbG9yOiB3aGl0ZTtcbn1cblxuLkFwcC1pbnRybyB7XG4gIGZvbnQtc2l6ZTogbGFyZ2U7XG59XG5cbkBrZXlmcmFtZXMgQXBwLWxvZ28tc3BpbiB7XG4gIGZyb20ge1xuICAgIHRyYW5zZm9ybTogcm90YXRlKDBkZWcpO1xuICB9XG4gIHRvIHtcbiAgICB0cmFuc2Zvcm06IHJvdGF0ZSgzNjBkZWcpO1xuICB9XG59XG4ifSx7Im5hbWUiOiJzcmMvbG9nby5zdmciLCJjb250ZW50IjoiPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgdmlld0JveD1cIjAgMCA4NDEuOSA1OTUuM1wiPlxuICAgIDxnIGZpbGw9XCIjREI0RDNGXCI+XG4gICAgICAgIDxwYXRoIGQ9XCJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40elwiLz5cbiAgICAgICAgPGNpcmNsZSBjeD1cIjQyMC45XCIgY3k9XCIyOTYuNVwiIHI9XCI0NS43XCIvPlxuICAgICAgICA8cGF0aCBkPVwiTTUyMC41IDc4LjF6XCIvPlxuICAgIDwvZz5cbjwvc3ZnPlxuIn0seyJuYW1lIjoic3JjL0FwcC5yZSIsImNvbnRlbnQiOiJbJWJzLnJhdyB7fHJlcXVpcmUoJy4vQXBwLmNzcycpfH1dO1xuXG5bQGJzLm1vZHVsZV0gZXh0ZXJuYWwgbG9nbyA6IHN0cmluZyA9IFwiLi9sb2dvLnN2Z1wiO1xuXG5sZXQgY29tcG9uZW50ID0gUmVhc29uUmVhY3Quc3RhdGVsZXNzQ29tcG9uZW50KFwiQXBwXCIpO1xuXG5sZXQgbWFrZSA9ICh+bWVzc2FnZSwgX2NoaWxkcmVuKSA9PiB7XG4gIC4uLmNvbXBvbmVudCxcbiAgcmVuZGVyOiBfc2VsZiA9PlxuICAgIDxkaXYgY2xhc3NOYW1lPVwiQXBwXCI+XG4gICAgICA8ZGl2IGNsYXNzTmFtZT1cIkFwcC1oZWFkZXJcIj5cbiAgICAgICAgPGltZyBzcmM9bG9nbyBjbGFzc05hbWU9XCJBcHAtbG9nb1wiIGFsdD1cImxvZ29cIiAvPlxuICAgICAgICA8aDI+IChSZWFzb25SZWFjdC5zdHJpbmcobWVzc2FnZSkpIDwvaDI+XG4gICAgICA8L2Rpdj5cbiAgICAgIDxwIGNsYXNzTmFtZT1cIkFwcC1pbnRyb1wiPlxuICAgICAgICAoUmVhc29uUmVhY3Quc3RyaW5nKFwiVG8gZ2V0IHN0YXJ0ZWQsIGVkaXRcIikpXG4gICAgICAgIDxjb2RlPiAoUmVhc29uUmVhY3Quc3RyaW5nKFwiIHNyYy9BcHAucmUgXCIpKSA8L2NvZGU+XG4gICAgICAgIChSZWFzb25SZWFjdC5zdHJpbmcoXCJhbmQgc2F2ZSB0byByZWxvYWQuXCIpKVxuICAgICAgPC9wPlxuICAgIDwvZGl2Pixcbn07XG4ifSx7Im5hbWUiOiJwdWJsaWMvaW5kZXguaHRtbCIsImNvbnRlbnQiOiI8IURPQ1RZUEUgaHRtbD5cbjxodG1sIGxhbmc9XCJlblwiPlxuICA8aGVhZD5cbiAgICA8bWV0YSBjaGFyc2V0PVwidXRmLThcIj5cbiAgICA8bWV0YSBuYW1lPVwidmlld3BvcnRcIiBjb250ZW50PVwid2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEsIHNocmluay10by1maXQ9bm9cIj5cbiAgICA8bWV0YSBuYW1lPVwidGhlbWUtY29sb3JcIiBjb250ZW50PVwiIzAwMDAwMFwiPlxuICAgIDwhLS1cbiAgICAgIG1hbmlmZXN0Lmpzb24gcHJvdmlkZXMgbWV0YWRhdGEgdXNlZCB3aGVuIHlvdXIgd2ViIGFwcCBpcyBhZGRlZCB0byB0aGVcbiAgICAgIGhvbWVzY3JlZW4gb24gQW5kcm9pZC4gU2VlIGh0dHBzOi8vZGV2ZWxvcGVycy5nb29nbGUuY29tL3dlYi9mdW5kYW1lbnRhbHMvZW5nYWdlLWFuZC1yZXRhaW4vd2ViLWFwcC1tYW5pZmVzdC9cbiAgICAtLT5cbiAgICA8bGluayByZWw9XCJtYW5pZmVzdFwiIGhyZWY9XCIlUFVCTElDX1VSTCUvbWFuaWZlc3QuanNvblwiPlxuICAgIDxsaW5rIHJlbD1cInNob3J0Y3V0IGljb25cIiBocmVmPVwiJVBVQkxJQ19VUkwlL2Zhdmljb24uaWNvXCI+XG4gICAgPCEtLVxuICAgICAgTm90aWNlIHRoZSB1c2Ugb2YgJVBVQkxJQ19VUkwlIGluIHRoZSB0YWdzIGFib3ZlLlxuICAgICAgSXQgd2lsbCBiZSByZXBsYWNlZCB3aXRoIHRoZSBVUkwgb2YgdGhlIGBwdWJsaWNgIGZvbGRlciBkdXJpbmcgdGhlIGJ1aWxkLlxuICAgICAgT25seSBmaWxlcyBpbnNpZGUgdGhlIGBwdWJsaWNgIGZvbGRlciBjYW4gYmUgcmVmZXJlbmNlZCBmcm9tIHRoZSBIVE1MLlxuXG4gICAgICBVbmxpa2UgXCIvZmF2aWNvbi5pY29cIiBvciBcImZhdmljb24uaWNvXCIsIFwiJVBVQkxJQ19VUkwlL2Zhdmljb24uaWNvXCIgd2lsbFxuICAgICAgd29yayBjb3JyZWN0bHkgYm90aCB3aXRoIGNsaWVudC1zaWRlIHJvdXRpbmcgYW5kIGEgbm9uLXJvb3QgcHVibGljIFVSTC5cbiAgICAgIExlYXJuIGhvdyB0byBjb25maWd1cmUgYSBub24tcm9vdCBwdWJsaWMgVVJMIGJ5IHJ1bm5pbmcgYG5wbSBydW4gYnVpbGRgLlxuICAgIC0tPlxuICAgIDx0aXRsZT5SZWFjdCBBcHA8L3RpdGxlPlxuICA8L2hlYWQ+XG4gIDxib2R5PlxuICAgIDxub3NjcmlwdD5cbiAgICAgIFlvdSBuZWVkIHRvIGVuYWJsZSBKYXZhU2NyaXB0IHRvIHJ1biB0aGlzIGFwcC5cbiAgICA8L25vc2NyaXB0PlxuICAgIDxkaXYgaWQ9XCJyb290XCI+PC9kaXY+XG4gICAgPCEtLVxuICAgICAgVGhpcyBIVE1MIGZpbGUgaXMgYSB0ZW1wbGF0ZS5cbiAgICAgIElmIHlvdSBvcGVuIGl0IGRpcmVjdGx5IGluIHRoZSBicm93c2VyLCB5b3Ugd2lsbCBzZWUgYW4gZW1wdHkgcGFnZS5cblxuICAgICAgWW91IGNhbiBhZGQgd2ViZm9udHMsIG1ldGEgdGFncywgb3IgYW5hbHl0aWNzIHRvIHRoaXMgZmlsZS5cbiAgICAgIFRoZSBidWlsZCBzdGVwIHdpbGwgcGxhY2UgdGhlIGJ1bmRsZWQgc2NyaXB0cyBpbnRvIHRoZSA8Ym9keT4gdGFnLlxuXG4gICAgICBUbyBiZWdpbiB0aGUgZGV2ZWxvcG1lbnQsIHJ1biBgbnBtIHN0YXJ0YCBvciBgeWFybiBzdGFydGAuXG4gICAgICBUbyBjcmVhdGUgYSBwcm9kdWN0aW9uIGJ1bmRsZSwgdXNlIGBucG0gcnVuIGJ1aWxkYCBvciBgeWFybiBidWlsZGAuXG4gICAgLS0+XG4gIDwvYm9keT5cbjwvaHRtbD5cbiJ9LHsibmFtZSI6ImJzY29uZmlnLmpzb24iLCJjb250ZW50Ijoie1xuICBcIm5hbWVcIjogXCJyZWFzb24tc2NyaXB0c1wiLFxuICBcInNvdXJjZXNcIjogW1wic3JjXCJdLFxuICBcImJzLWRlcGVuZGVuY2llc1wiOiBbXCJyZWFzb24tcmVhY3RcIiwgXCJAZ2xlbm5zbC9icy1qZXN0XCJdLFxuICBcInJlYXNvblwiOiB7XG4gICAgXCJyZWFjdC1qc3hcIjogMlxuICB9LFxuICBcImJzYy1mbGFnc1wiOiBbXCItYnMtc3VwZXItZXJyb3JzXCJdLFxuICBcInJlZm10XCI6IDMsXG4gIFwicGFja2FnZS1zcGVjc1wiOiB7XG4gICAgXCJtb2R1bGVcIjogXCJlczZcIixcbiAgICBcImluLXNvdXJjZVwiOiB0cnVlXG4gIH0sXG4gIFwic3VmZml4XCI6IFwiLmJzLmpzXCJcbn1cbiJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCIsImNvbmZpZyI6eyJpc1NlcnZlciI6dHJ1ZX19LCJmbG93Ijp7ImRpc3BsYXlOYW1lIjoiRmxvdyIsInRhZ2xpbmUiOiJBIHN0YXRpYyB0eXBlIGNoZWNrZXIgZm9yIEphdmFTY3JpcHQiLCJrZXkiOiJmbG93IiwiZW50cnlwb2ludCI6InNyYy9pbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoZWFkZXIiOiJub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9mbG93LnN2ZyIsInByb2plY3RfdGVtcGxhdGUiOlt7Im5hbWUiOiJzcmMvaW5kZXguanMiLCJjb250ZW50IjoiLy8gQGZsb3dcbmNvbnN0IG1hdGggPSByZXF1aXJlKCcuL21hdGgnKTtcblxuY29uc29sZS5sb2cobWF0aC5zcXVhcmUoNykpO1xuY29uc29sZS5sb2cobWF0aC5hZGQoXCJhXCIsIFwiYlwiKSk7XG4ifSx7Im5hbWUiOiJzcmMvbWF0aC5qcyIsImNvbnRlbnQiOiIvLyBAZmxvd1xuXG5leHBvcnRzLmFkZCA9ICh4OiBudW1iZXIsIHk6IG51bWJlcikgPT4geCArIHk7XG5leHBvcnRzLnNxdWFyZSA9ICh4OiBudW1iZXIpID0+IHggKiB4O1xuIn0seyJuYW1lIjoicGFja2FnZS5qc29uIiwiY29udGVudCI6IntcbiAgXCJuYW1lXCI6IFwibXktcHJvamVjdFwiLFxuICBcIm1haW5cIjogXCJzcmMvaW5kZXguanNcIixcbiAgXCJzY3JpcHRzXCI6IHtcbiAgICBcInN0YXJ0XCI6IFwiZmxvdy1ub2RlIC1hIHNyYy9pbmRleC5qc1wiXG4gIH0sXG4gIFwiZGVwZW5kZW5jaWVzXCI6IHtcbiAgICBcImZsb3ctcmVtb3ZlLXR5cGVzXCI6IFwiXjEuMi4zXCIsXG4gICAgXCJmbG93LWJpblwiOiBcIl4wLjc1LjBcIlxuICB9XG59In0seyJuYW1lIjoiLmZsb3djb25maWciLCJjb250ZW50IjoiW2lnbm9yZV1cblxuW2luY2x1ZGVdXG5cbltsaWJzXVxuXG5bbGludHNdXG5cbltvcHRpb25zXVxuXG5bc3RyaWN0XSJ9XSwibWF0Y2hpbmdzIjpbWyJ7IiwifSJdLFsiKCIsIikiXSxbIlsiLCJdIl1dLCJlbmdpbmUiOiJnb3ZhbCJ9LCJiYXNoIjp7ImRpc3BsYXlOYW1lIjoiYmFzaCIsInRhZ2xpbmUiOiJUaGUgY2xhc3NpYyBVbml4IHNoZWxsIiwia2V5IjoiYmFzaCIsImVudHJ5cG9pbnQiOiJtYWluLnNoIiwiZXh0Ijoic2giLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoiR05VIGJhc2gsIHZlcnNpb24gNC40LjEyKDEpLXJlbGVhc2UgKHg4Nl82NC1wYy1saW51eC1nbnUpIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsInRlbXBsYXRlIjoiZWNobyBIZWxsbyBXb3JsZCIsIm1hdGNoaW5ncyI6W1sieyIsIn0iXSxbIigiLCIpIl0sWyJbIiwiXSJdXSwiZW5naW5lIjoiZ292YWwifSwicXVpbCI6eyJkaXNwbGF5TmFtZSI6IlF1aWwiLCJ0YWdsaW5lIjoiQSBxdWFudHVtIGluc3RydWN0aW9uIGxhbmd1YWdlLiIsImtleSI6InF1aWwiLCJlbnRyeXBvaW50IjoibWFpbi5xdWlsIiwiZXh0IjoicXVpbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc0V2YWwiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGVhZGVyIjoiUHlxdWlsIDEuOS4wLCBQeXRob24gMy42LjEiLCJjYXRlZ29yeSI6IlF1YW50dW0iLCJpY29uIjoiIiwidGVtcGxhdGUiOiIiLCJtYXRjaGluZ3MiOltdLCJlbmdpbmUiOiJnb3ZhbCJ9fQ=='))</script><script src="./hello_files/api.js.download"></script><style type="text/css" data-styled-jsx=""></style><script type="text/javascript" src="./hello_files/monaco.12f69cc02e5f71a8a143.bundle.js.download"></script><script type="text/javascript" charset="utf-8" async="" src="./hello_files/app_components_PortalWrapper_react_22329ba4098c3d2fe8ed216ad3171ecd-8573c1a017e6e37caba9.js.download"></script><script type="text/javascript" charset="utf-8" async="" src="./hello_files/app_workspace_plugins_editor_monaco_Monaco_react_6212bc299b7eccc161785b5f7f063afe-004f0c7669369084c915.js.download"></script><style>.grecaptcha-badge:hover { left: 4px !important }</style><meta property="og:title" content="SoggyKnobbyProducts" class="next-head"><meta name="twitter:title" content="SoggyKnobbyProducts" class="next-head"><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor font */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", "Ubuntu", "Droid Sans", sans-serif;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-label:focus {
	color: #0059AC;
	stroke-width: 1.2px;
	text-shadow: 0px 0px 0.15px #0059AC;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-item .action-label:focus,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-item .action-label:focus {
	color: #ACDDFF;
	stroke-width: 1.2px;
	text-shadow: 0px 0px 0.15px #ACDDFF;
}

.monaco-editor-hover p {
	margin: 0;
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* tree */
	.monaco-editor.vs .monaco-tree .monaco-tree-row,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-tree .monaco-tree-row.selected,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row.selected,
	.monaco-editor.vs .monaco-tree .monaco-tree-row.focused,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-tree .monaco-tree-row:hover,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-item .action-label:focus,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-item .action-label:focus {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-item .action-label:hover,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-item .action-label:hover {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
	-webkit-font-feature-settings: "liga" off, "calt" off;
	font-feature-settings: "liga" off, "calt" off;
}
.monaco-editor.enable-ligatures {
	-webkit-font-feature-settings: "liga" on, "calt" on;
	font-feature-settings: "liga" on, "calt" on;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .vs-whitespace {
	display:inline-block;
}

</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers {
	cursor: -webkit-image-set(
		url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNSIgaGVpZ2h0PSIyMSIgeD0iMHB4IiB5PSIwcHgiIHZpZXdCb3g9IjAgMCAxNSAyMSIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTUgMjE7Ij48cG9seWdvbiBzdHlsZT0iZmlsbDojRkZGRkZGO3N0cm9rZTojMDAwMDAwIiBwb2ludHM9IjE0LjUsMS4yIDEuOSwxMy44IDcuMSwxMy44IDQuNSwxOS4xIDcuNywyMC4xIDEwLjMsMTQuOSAxNC41LDE4Ii8+PC9zdmc+") 1x,
		url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMzAiIGhlaWdodD0iNDIiIHZpZXdCb3g9IjAgMCAzMCA0MiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMzAgNDI7Ij48cG9seWdvbiBzdHlsZT0iZmlsbDojRkZGRkZGO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyOyIgcG9pbnRzPSIyOSwyLjQgMy44LDI3LjYgMTQuMywyNy42IDksMzguMSAxNS40LDQwLjIgMjAuNiwyOS43IDI5LDM2Ii8+PC9zdmc+Cg==") 2x
	) 30 0, default;
}

.monaco-editor.mac .margin-view-overlays .line-numbers {
	cursor: -webkit-image-set(
		url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxOCIgdmlld0JveD0iMCAwIDEyIDE4Ij48c3R5bGU+LnN0MHtmaWxsOiNmZmZ9PC9zdHlsZT48dGl0bGU+ZmxpcHBlZC1jdXJzb3ItbWFjPC90aXRsZT48cGF0aCBkPSJNNC4zIDE2LjVsMS42LTQuNkgxLjFMMTEuNSAxLjJ2MTQuNEw4LjcgMTNsLTEuNiA0LjV6Ii8+PHBhdGggY2xhc3M9InN0MCIgZD0iTTExIDE0LjVsLTIuNS0yLjNMNyAxNi43IDUgMTZsMS42LTQuNWgtNGw4LjUtOU0wIDEyLjVoNS4ybC0xLjUgNC4xTDcuNSAxOCA5IDE0LjJsMi45IDIuM1YwTDAgMTIuNXoiLz48L3N2Zz4=") 1x,
		url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIzNiIgdmlld0JveD0iMCAwIDI0IDM2LjEiPjxkZWZzPjxzdHlsZT4uYXtmaWxsOiNmZmY7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5mbGlwcGVkLWN1cnNvci1tYWMtMng8L3RpdGxlPjxwb2x5Z29uIHBvaW50cz0iOC42IDMzLjEgMTEuOCAyMy45IDIuMiAyMy45IDIzIDIuNSAyMyAzMS4zIDE3LjQgMjYuMSAxNC4yIDM1LjEgOC42IDMzLjEiLz48cGF0aCBjbGFzcz0iYSIgZD0iTTIyLDI5LjFsLTUtNC42LTMuMDYyLDguOTM4LTQuMDYyLTEuNUwxMywyM0g1TDIyLDVNMCwyNUgxMC40bC0zLDguM0wxNSwzNi4xbDMuMTI1LTcuNjYyTDI0LDMzVjBaIi8+PC9zdmc+") 2x
	) 24 3, default;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cigr = core ident guides rendering (div)
*/
.monaco-editor .lines-content .cigr {
	position: absolute;
}
.monaco-editor .lines-content .cigra {
	position: absolute;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.monaco-editor.safari .lines-content,
.monaco-editor.safari .view-line,
.monaco-editor.safari .view-lines {
	-webkit-user-select: text;
	user-select: text;
}

.monaco-editor .lines-content,
.monaco-editor .view-line,
.monaco-editor .view-lines {
	-webkit-user-select: none;
	-ms-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-o-user-select: none;
	user-select: none;
}

.monaco-editor .view-lines {
	cursor: text;
	white-space: nowrap;
}

.monaco-editor.vs-dark.mac .view-lines,
.monaco-editor.hc-black.mac .view-lines {
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAL0lEQVQoz2NgCD3x//9/BhBYBWdhgFVAiVW4JBFKGIa4AqD0//9D3pt4I4tAdAMAHTQ/j5Zom30AAAAASUVORK5CYII=) 1x, url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAz0lEQVRIx2NgYGBY/R8I/vx5eelX3n82IJ9FxGf6tksvf/8FiTMQAcAGQMDvSwu09abffY8QYSAScNk45G198eX//yev73/4///701eh//kZSARckrNBRvz//+8+6ZohwCzjGNjdgQxkAg7B9WADeBjIBqtJCbhRA0YNoIkBSNmaPEMoNmA0FkYNoFKhapJ6FGyAH3nauaSmPfwI0v/3OukVi0CIZ+F25KrtYcx/CTIy0e+rC7R1Z4KMICVTQQ14feVXIbR695u14+Ir4gwAAD49E54wc1kWAAAAAElFTkSuQmCC) 2x) 5 8, text;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	cursor: text;
	overflow: hidden;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .up-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiIGZpbGw9IiM0MjQyNDIiLz48L3N2Zz4=");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .down-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTE4MCA1LjQ5MDQ1OTkxODk3NTgzLDUuODExNTAwMDcyNDc5MjQ4KSIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiLz48L3N2Zz4=");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .left-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDUuNDkwNDU5OTE4OTc1ODMxLDUuNDMxMzgyMTc5MjYwMjU0KSIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNDgwNDYsOC41ODEzOGwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .right-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoOTAgNS42MTcxNjUwODg2NTM1NjQ1LDUuNTU4MDg5NzMzMTIzNzgpICIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNjA3MTcsOC43MDgwOWwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
	cursor: pointer;
}

.hc-black .monaco-scrollable-element > .scrollbar > .up-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .up-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiIGZpbGw9IiNFOEU4RTgiLz48L3N2Zz4=");
}
.hc-black .monaco-scrollable-element > .scrollbar > .down-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .down-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTE4MCA1LjQ5MDQ1OTkxODk3NTgzLDUuODExNTAwMDcyNDc5MjQ4KSIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiLz48L3N2Zz4=");
}
.hc-black .monaco-scrollable-element > .scrollbar > .left-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .left-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDUuNDkwNDU5OTE4OTc1ODMxLDUuNDMxMzgyMTc5MjYwMjU0KSIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNDgwNDYsOC41ODEzOGwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
}
.hc-black .monaco-scrollable-element > .scrollbar > .right-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .right-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoOTAgNS42MTcxNjUwODg2NTM1NjQ1LDUuNTU4MDg5NzMzMTIzNzgpICIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNjA3MTcsOC43MDgwOWwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	-webkit-transition: opacity 100ms linear;
	-o-transition: opacity 100ms linear;
	-moz-transition: opacity 100ms linear;
	-ms-transition: opacity 100ms linear;
	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	-webkit-transition: opacity 800ms linear;
	-o-transition: opacity 800ms linear;
	-moz-transition: opacity 800ms linear;
	-ms-transition: opacity 800ms linear;
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
	box-shadow: #DDD 0 6px 6px -6px inset;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
	box-shadow: #DDD 6px 0 6px -6px inset;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top.left {
	box-shadow: #DDD 6px 6px 6px -6px inset;
}

/* ---------- Default Style ---------- */

.vs .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(100, 100, 100, .4);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(121, 121, 121, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(111, 195, 223, .6);
}

.monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(100, 100, 100, .7);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(111, 195, 223, .8);
}

.monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(0, 0, 0, .6);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(191, 191, 191, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(111, 195, 223, 1);
}

.vs-dark .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.vs-dark .monaco-scrollable-element .shadow.left {
	box-shadow: #000 6px 0 6px -6px inset;
}

.vs-dark .monaco-scrollable-element .shadow.top.left {
	box-shadow: #000 6px 6px 6px -6px inset;
}

.hc-black .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.left {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.top.left {
	box-shadow: none;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-diff-editor .diffViewport {
	box-shadow: inset 0px 0px 1px 0px #B9B9B9;
	background: rgba(0, 0, 0, 0.10);
}

.monaco-diff-editor.vs-dark .diffViewport,
.monaco-diff-editor.hc-black .diffViewport {
	background: rgba(255, 255, 255, 0.10);
}
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	background-size: 60%;
	opacity: 0.7;
	background-repeat: no-repeat;
	background-position: 50% 50%;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	opacity: 1;
}
.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPkxheWVyIDE8L3RpdGxlPjxyZWN0IGhlaWdodD0iMTEiIHdpZHRoPSIzIiB5PSIzIiB4PSI3IiBmaWxsPSIjNDI0MjQyIi8+PHJlY3QgaGVpZ2h0PSIzIiB3aWR0aD0iMTEiIHk9IjciIHg9IjMiIGZpbGw9IiM0MjQyNDIiLz48L3N2Zz4=");
}
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPkxheWVyIDE8L3RpdGxlPjxyZWN0IGhlaWdodD0iMyIgd2lkdGg9IjExIiB5PSI3IiB4PSIzIiBmaWxsPSIjNDI0MjQyIi8+PC9zdmc+");
}

.monaco-editor.vs-dark .insert-sign,
.monaco-diff-editor.vs-dark .insert-sign,
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPkxheWVyIDE8L3RpdGxlPjxyZWN0IGhlaWdodD0iMTEiIHdpZHRoPSIzIiB5PSIzIiB4PSI3IiBmaWxsPSIjQzVDNUM1Ii8+PHJlY3QgaGVpZ2h0PSIzIiB3aWR0aD0iMTEiIHk9IjciIHg9IjMiIGZpbGw9IiNDNUM1QzUiLz48L3N2Zz4=");
}
.monaco-editor.vs-dark .delete-sign,
.monaco-diff-editor.vs-dark .delete-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPkxheWVyIDE8L3RpdGxlPjxyZWN0IGhlaWdodD0iMyIgd2lkdGg9IjExIiB5PSI3IiB4PSIzIiBmaWxsPSIjQzVDNUM1Ii8+PC9zdmc+");
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

.monaco-editor .diagonal-fill {
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5FVCB2My41LjEwMPRyoQAAAChJREFUKFNjOH/+fAMDDgCSu3Dhwn9c8gwwBTgNGR4KQP4HhQOhsAIAZCBTkhtqePcAAAAASUVORK5CYII=");
}
.monaco-editor.vs-dark .diagonal-fill {
	opacity: 0.2;
}
.monaco-editor.hc-black .diagonal-fill {
	background: none;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-sash {
	position: absolute;
	z-index: 90;
	touch-action: none;
}

.monaco-sash.vertical {
	cursor: ew-resize;
	height: 100%;
	top: 0;
}

.monaco-sash.horizontal {
	cursor: ns-resize;
	width: 100%;
	left: 0;
}

.monaco-sash.disabled {
	cursor: default !important;
}

/** Custom Mac Cursor */

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-builder-hidden {
	display: none !important;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	-webkit-user-select: none;
	-ms-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-o-user-select: none;
	user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-cell {
	display: table-cell;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}
.monaco-diff-editor .action-label.icon.close-diff-review {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iIzQyNDI0MiIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==") center center no-repeat;
}
.monaco-diff-editor.hc-black .action-label.icon.close-diff-review,
.monaco-diff-editor.vs-dark .action-label.icon.close-diff-review {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iI2U4ZThlOCIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==") center center no-repeat;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	text-align: right;
	overflow: hidden;
	white-space: nowrap;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	width: 100%;
	justify-content: flex-end;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar.reverse .actions-container {
	flex-direction: row-reverse;
}

.monaco-action-bar .action-item {
	cursor: pointer;
	display: inline-block;
	-ms-transition: -ms-transform 50ms ease;
	-webkit-transition: -webkit-transform 50ms ease;
	-moz-transition: -moz-transform 50ms ease;
	-o-transition: -o-transform 50ms ease;
	transition: transform 50ms ease;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar.animated .action-item.active {
	-ms-transform: scale(1.272019649, 1.272019649); /* 1.272019649 = √φ */
	-webkit-transform: scale(1.272019649, 1.272019649);
	-moz-transform: scale(1.272019649, 1.272019649);
	-o-transform: scale(1.272019649, 1.272019649);
	transform: scale(1.272019649, 1.272019649);
}

.monaco-action-bar .action-item .icon {
	display: inline-block;
}

.monaco-action-bar .action-label {
	font-size: 12px;
	margin-right: 0.3em;
}

.monaco-action-bar .action-label.octicon {
	font-size: 15px;
	line-height: 35px;
	text-align: center;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.4;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar.animated.vertical .action-item.active {
	-ms-transform: translate(5px, 0);
	-webkit-transform: translate(5px, 0);
	-moz-transform: translate(5px, 0);
	-o-transform: translate(5px, 0);
	transform: translate(5px, 0);
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	margin-right: 10px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-select-box {
	width: 100%;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-select-box-dropdown-container {
	display: none;
}

.monaco-select-box-dropdown-container.visible {
	display: flex;
	flex-direction: column;
	text-align: left;
	width: 1px;
	overflow: hidden;
}

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container {
	flex: 0 0 auto;
	align-self: flex-start;
	padding-bottom: 1px;
	padding-top: 1px;
	padding-left: 1px;
	padding-right: 1px;
	width: 100%;
	overflow: hidden;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
}

.hc-black .monaco-select-box-dropdown-container > .select-box-dropdown-list-container {
	padding-bottom: 4px;
	padding-top: 3px;
}

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container .monaco-list .monaco-list-row > .option-text {
	text-overflow: ellipsis;
	overflow: hidden;
	padding-left: 3.5px;
	white-space: nowrap;
}

.monaco-select-box-dropdown-container > .select-box-dropdown-container-width-control {
	flex: 1 1 auto;
	align-self: flex-start;
	opacity: 0;
}

.monaco-select-box-dropdown-container > .select-box-dropdown-container-width-control > .width-control-div {
	overflow: hidden;
	max-height: 0px;
}

.monaco-select-box-dropdown-container > .select-box-dropdown-container-width-control > .width-control-div > .option-text-width-control {
	padding-left: 4px;
	padding-right: 8px;
	white-space: nowrap;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: -moz-none;
	-ms-user-select: none;
	-o-user-select: none;
	user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list-row {
	position: absolute;
	-moz-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	cursor: pointer;
	overflow: hidden;
	width: 100%;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused, .monaco-list.selection-single, .monaco-list.selection-multiple {
	outline: 0 !important;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view .monaco-menu {
	min-width: 130px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-menu .monaco-action-bar.vertical {
	margin-left: 0;
}

.monaco-menu .monaco-action-bar.vertical .actions-container {
	display: block;
}

.monaco-menu .monaco-action-bar.vertical .action-item {
	padding: 0;
	-ms-transform: none;
	-webkit-transform: none;
	-moz-transform: none;
	-o-transform: none;
	transform: none;
	display: -ms-flexbox;
	display: flex;
}

.monaco-menu .monaco-action-bar.vertical .action-item.active {
	-ms-transform: none;
	-webkit-transform: none;
	-moz-transform: none;
	-o-transform: none;
	transform: none;
}

.monaco-menu .monaco-action-bar.vertical .action-item.focused {
	background-color: #E4E4E4;
}

.monaco-menu .monaco-action-bar.vertical .action-item:hover:not(.disabled) {
	background-color: #EEE;
}

.monaco-menu .monaco-action-bar.vertical .action-label {
	-ms-flex: 1 1 auto;
	flex: 1 1 auto;
	text-decoration: none;
	padding: 0.8em 1em;
	line-height: 1.1em;
	background: none;
}

.monaco-menu .monaco-action-bar.vertical .keybinding {
	display: inline-block;
	-ms-flex: 2 1 auto;
	flex: 2 1 auto;
	padding: 0.8em 1em;
	line-height: 1.1em;
	font-size: 12px;
	text-align: right;
}

.monaco-menu .monaco-action-bar.vertical .action-item.disabled .keybinding {
	opacity: 0.4;
}

.monaco-menu .monaco-action-bar.vertical .action-label:not(.separator) {
	display: inline-block;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	margin: 0;
}

.monaco-menu .monaco-action-bar.vertical .action-label.separator {
	padding: 0.5em 0 0 0;
	margin-bottom: 0.5em;
	width: 100%;
}

.monaco-menu .monaco-action-bar.vertical .action-label.separator.text {
	padding: 0.7em 1em 0.1em 1em;
	font-weight: bold;
	opacity: 1;
}

.monaco-menu .monaco-action-bar.vertical .action-label:hover {
	color: inherit;
}

/* Context Menu */

.context-view.monaco-menu-container {
	font-family: "Segoe WPC", "Segoe UI", ".SFNSDisplay-Light", "SFUIText-Light", "HelveticaNeue-Light", sans-serif, "Droid Sans Fallback";
	outline: 0;
	box-shadow: 0 2px 8px #A8A8A8;
	border: none;
	color: #646465;
	background-color: white;
	-webkit-animation: fadeIn 0.083s linear;
	-o-animation: fadeIn 0.083s linear;
	-moz-animation: fadeIn 0.083s linear;
	-ms-animation: fadeIn 0.083s linear;
	animation: fadeIn 0.083s linear;
}

.context-view.monaco-menu-container :focus {
	outline: 0;
}

/* Dark theme */
.vs-dark .monaco-menu .monaco-action-bar.vertical .action-item.focused {
	background-color: #4B4C4D;
}

.vs-dark .monaco-menu .monaco-action-bar.vertical .action-item:hover:not(.disabled) {
	background-color: #3A3A3A;
}

.vs-dark .context-view.monaco-menu-container {
	box-shadow: 0 2px 8px #000;
	color: #BBB;
	background-color: #2D2F31;
}

/* High Contrast Theming */
.hc-black .context-view.monaco-menu-container {
	border: 2px solid #6FC3DF;
	color: white;
	background-color: #0C141F;
	box-shadow: none;
}

.hc-black .monaco-menu .monaco-action-bar.vertical .action-item.focused {
	background: none;
	border: 1px dotted #f38518;
}

.hc-black .monaco-menu .monaco-action-bar.vertical .action-item:hover:not(.disabled) {
	background: none;
	border: 1px dashed #f38518;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
	z-index: 1000;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-tree {
	height: 100%;
	width: 100%;
	white-space: nowrap;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: -moz-none;
	-ms-user-select: none;
	-o-user-select: none;
	user-select: none;
	position: relative;
}

.monaco-tree > .monaco-scrollable-element {
	height: 100%;
}

.monaco-tree > .monaco-scrollable-element > .monaco-tree-wrapper {
	height: 100%;
	width: 100%;
	position: relative;
}

.monaco-tree .monaco-tree-rows {
	position: absolute;
	width: 100%;
	height: 100%;
}

.monaco-tree .monaco-tree-rows > .monaco-tree-row {
	-moz-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	cursor: pointer;
	overflow: hidden;
	width: 100%;
	touch-action: none;
}

.monaco-tree .monaco-tree-rows > .monaco-tree-row > .content {
	position: relative;
	height: 100%;
}

.monaco-tree-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
}

/* for OS X ballistic scrolling */
.monaco-tree .monaco-tree-rows > .monaco-tree-row.scrolling {
	display: none;
}

/* Expansion */

.monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.has-children > .content:before {
	content: ' ';
	position: absolute;
	display: block;
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iIzY0NjQ2NSIgZD0iTTYgNHY4bDQtNC00LTR6bTEgMi40MTRMOC41ODYgOCA3IDkuNTg2VjYuNDE0eiIvPjwvc3ZnPg==") 50% 50% no-repeat;
	width: 16px;
	height: 100%;
	top: 0;
	left: -16px;
}

.monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.expanded > .content:before {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iIzY0NjQ2NSIgZD0iTTExIDEwSDUuMzQ0TDExIDQuNDE0VjEweiIvPjwvc3ZnPg==");
}

.monaco-tree .monaco-tree-rows > .monaco-tree-row.has-children.loading > .content:before {
	background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0nMS4wJyBzdGFuZGFsb25lPSdubycgPz4KPHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZlcnNpb249JzEuMScgd2lkdGg9JzEwcHgnIGhlaWdodD0nMTBweCc+Cgk8c3R5bGU+CiAgICBjaXJjbGUgewogICAgICBhbmltYXRpb246IGJhbGwgMC42cyBsaW5lYXIgaW5maW5pdGU7CiAgICB9CgogICAgY2lyY2xlOm50aC1jaGlsZCgyKSB7IGFuaW1hdGlvbi1kZWxheTogMC4wNzVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDMpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjE1czsgfQogICAgY2lyY2xlOm50aC1jaGlsZCg0KSB7IGFuaW1hdGlvbi1kZWxheTogMC4yMjVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDUpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjNzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDYpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjM3NXM7IH0KICAgIGNpcmNsZTpudGgtY2hpbGQoNykgeyBhbmltYXRpb24tZGVsYXk6IDAuNDVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDgpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjUyNXM7IH0KCiAgICBAa2V5ZnJhbWVzIGJhbGwgewogICAgICBmcm9tIHsgb3BhY2l0eTogMTsgfQogICAgICB0byB7IG9wYWNpdHk6IDAuMzsgfQogICAgfQoJPC9zdHlsZT4KCTxnPgoJCTxjaXJjbGUgY3g9JzUnIGN5PScxJyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzcuODI4NCcgY3k9JzIuMTcxNicgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PSc5JyBjeT0nNScgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PSc3LjgyODQnIGN5PSc3LjgyODQnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nNScgY3k9JzknIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nMi4xNzE2JyBjeT0nNy44Mjg0JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzEnIGN5PSc1JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzIuMTcxNicgY3k9JzIuMTcxNicgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCTwvZz4KPC9zdmc+Cg==");
}

/* Highlighted */

.monaco-tree.highlighted .monaco-tree-rows > .monaco-tree-row:not(.highlighted) {
	opacity: 0.3;
}

.vs-dark .monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.has-children > .content:before {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI0U4RThFOCIgZD0iTTYgNHY4bDQtNC00LTR6bTEgMi40MTRMOC41ODYgOCA3IDkuNTg2VjYuNDE0eiIvPjwvc3ZnPg==");
}

.vs-dark .monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.expanded > .content:before {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI0U4RThFOCIgZD0iTTExIDEwSDUuMzQ0TDExIDQuNDE0VjEweiIvPjwvc3ZnPg==");
}

.vs-dark .monaco-tree .monaco-tree-rows > .monaco-tree-row.has-children.loading > .content:before {
	background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0nMS4wJyBzdGFuZGFsb25lPSdubycgPz4KPHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZlcnNpb249JzEuMScgd2lkdGg9JzEwcHgnIGhlaWdodD0nMTBweCc+Cgk8c3R5bGU+CiAgICBjaXJjbGUgewogICAgICBhbmltYXRpb246IGJhbGwgMC42cyBsaW5lYXIgaW5maW5pdGU7CiAgICB9CgogICAgY2lyY2xlOm50aC1jaGlsZCgyKSB7IGFuaW1hdGlvbi1kZWxheTogMC4wNzVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDMpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjE1czsgfQogICAgY2lyY2xlOm50aC1jaGlsZCg0KSB7IGFuaW1hdGlvbi1kZWxheTogMC4yMjVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDUpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjNzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDYpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjM3NXM7IH0KICAgIGNpcmNsZTpudGgtY2hpbGQoNykgeyBhbmltYXRpb24tZGVsYXk6IDAuNDVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDgpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjUyNXM7IH0KCiAgICBAa2V5ZnJhbWVzIGJhbGwgewogICAgICBmcm9tIHsgb3BhY2l0eTogMTsgfQogICAgICB0byB7IG9wYWNpdHk6IDAuMzsgfQogICAgfQoJPC9zdHlsZT4KCTxnIHN0eWxlPSJmaWxsOmdyZXk7Ij4KCQk8Y2lyY2xlIGN4PSc1JyBjeT0nMScgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PSc3LjgyODQnIGN5PScyLjE3MTYnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nOScgY3k9JzUnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nNy44Mjg0JyBjeT0nNy44Mjg0JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzUnIGN5PSc5JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzIuMTcxNicgY3k9JzcuODI4NCcgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PScxJyBjeT0nNScgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PScyLjE3MTYnIGN5PScyLjE3MTYnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+Cgk8L2c+Cjwvc3ZnPgo=");
}

.hc-black .monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.has-children > .content:before	{
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTYgNHY4bDQtNC00LTR6bTEgMi40MTRsMS41ODYgMS41ODYtMS41ODYgMS41ODZ2LTMuMTcyeiIvPjwvc3ZnPg==");
}

.hc-black .monaco-tree .monaco-tree-rows.show-twisties > .monaco-tree-row.expanded > .content:before {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTExIDEwLjA3aC01LjY1Nmw1LjY1Ni01LjY1NnY1LjY1NnoiLz48L3N2Zz4=");
}

.hc-black .monaco-tree .monaco-tree-rows > .monaco-tree-row.has-children.loading > .content:before {
	background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0nMS4wJyBzdGFuZGFsb25lPSdubycgPz4KPHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZlcnNpb249JzEuMScgd2lkdGg9JzEwcHgnIGhlaWdodD0nMTBweCc+Cgk8c3R5bGU+CiAgICBjaXJjbGUgewogICAgICBhbmltYXRpb246IGJhbGwgMC42cyBsaW5lYXIgaW5maW5pdGU7CiAgICB9CgogICAgY2lyY2xlOm50aC1jaGlsZCgyKSB7IGFuaW1hdGlvbi1kZWxheTogMC4wNzVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDMpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjE1czsgfQogICAgY2lyY2xlOm50aC1jaGlsZCg0KSB7IGFuaW1hdGlvbi1kZWxheTogMC4yMjVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDUpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjNzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDYpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjM3NXM7IH0KICAgIGNpcmNsZTpudGgtY2hpbGQoNykgeyBhbmltYXRpb24tZGVsYXk6IDAuNDVzOyB9CiAgICBjaXJjbGU6bnRoLWNoaWxkKDgpIHsgYW5pbWF0aW9uLWRlbGF5OiAwLjUyNXM7IH0KCiAgICBAa2V5ZnJhbWVzIGJhbGwgewogICAgICBmcm9tIHsgb3BhY2l0eTogMTsgfQogICAgICB0byB7IG9wYWNpdHk6IDAuMzsgfQogICAgfQoJPC9zdHlsZT4KCTxnIHN0eWxlPSJmaWxsOndoaXRlOyI+CgkJPGNpcmNsZSBjeD0nNScgY3k9JzEnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nNy44Mjg0JyBjeT0nMi4xNzE2JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzknIGN5PSc1JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJCTxjaXJjbGUgY3g9JzcuODI4NCcgY3k9JzcuODI4NCcgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PSc1JyBjeT0nOScgcj0nMScgc3R5bGU9J29wYWNpdHk6MC4zOycgLz4KCQk8Y2lyY2xlIGN4PScyLjE3MTYnIGN5PSc3LjgyODQnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nMScgY3k9JzUnIHI9JzEnIHN0eWxlPSdvcGFjaXR5OjAuMzsnIC8+CgkJPGNpcmNsZSBjeD0nMi4xNzE2JyBjeT0nMi4xNzE2JyByPScxJyBzdHlsZT0nb3BhY2l0eTowLjM7JyAvPgoJPC9nPgo8L3N2Zz4K");
}

.monaco-tree-action.collapse-all {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iLTEgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAtMSAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjNDI0MjQyIiBkPSJNMTQgMXY5aC0xdi04aC04di0xaDl6bS0xMSAydjFoOHY4aDF2LTloLTl6bTcgMnY5aC05di05aDl6bS0yIDJoLTV2NWg1di01eiIvPjxyZWN0IHg9IjQiIHk9IjkiIGZpbGw9IiMwMDUzOUMiIHdpZHRoPSIzIiBoZWlnaHQ9IjEiLz48L3N2Zz4=") center center no-repeat;
}

.hc-black .monaco-tree-action.collapse-all,
.vs-dark .monaco-tree-action.collapse-all {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iLTEgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAtMSAwIDE2IDE2Ij48cGF0aCBmaWxsPSIjQzVDNUM1IiBkPSJNMTQgMXY5aC0xdi04aC04di0xaDl6bS0xMSAydjFoOHY4aDF2LTloLTl6bTcgMnY5aC05di05aDl6bS0yIDJoLTV2NWg1di01eiIvPjxyZWN0IHg9IjQiIHk9IjkiIGZpbGw9IiM3NUJFRkYiIHdpZHRoPSIzIiBoZWlnaHQ9IjEiLz48L3N2Zz4=") center center no-repeat;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .bracket-match {
	box-sizing: border-box;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-menu .monaco-action-bar.vertical .action-label.hover {
	background-color: #EEE;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .codelens-decoration {
	overflow: hidden;
	display: inline-block;
	text-overflow: ellipsis;
}

.monaco-editor .codelens-decoration > span,
.monaco-editor .codelens-decoration > a {
	-moz-user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	user-select: none;
	white-space: nowrap;
	vertical-align: sub;
}

.monaco-editor .codelens-decoration > a {
	text-decoration: none;
}

.monaco-editor .codelens-decoration > a:hover {
	text-decoration: underline;
	cursor: pointer;
}

.monaco-editor .codelens-decoration.invisible-cl {
	opacity: 0;
}

@keyframes fadein { 0% { opacity:0; visibility:visible;} 100% { opacity:1; } }
@-moz-keyframes fadein { 0% { opacity:0; visibility:visible;} 100% { opacity:1; } }
@-o-keyframes fadein { 0% { opacity:0; visibility:visible;} 100% { opacity:1; } }
@-webkit-keyframes fadein { 0% { opacity:0; visibility:visible;} 100% { opacity:1; } }

.monaco-editor .codelens-decoration.fadein {
	-webkit-animation: fadein 0.5s linear;
	-moz-animation: fadein 0.5s linear;
	-o-animation: fadein 0.5s linear;
	animation: fadein 0.5s linear;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs .dnd-target {
	border-right: 2px dotted black;
	color: white; /* opposite of black */
}
.monaco-editor.vs-dark .dnd-target {
	border-right: 2px dotted #AEAFAD;
	color: #51504f; /* opposite of #AEAFAD */
}
.monaco-editor.hc-black .dnd-target {
	border-right: 2px dotted #fff;
	color: #000; /* opposite of #fff */
}

.monaco-editor.mouse-default .view-lines,
.monaco-editor.vs-dark.mac.mouse-default .view-lines,
.monaco-editor.hc-black.mac.mouse-default .view-lines {
	cursor: default;
}
.monaco-editor.mouse-copy .view-lines,
.monaco-editor.vs-dark.mac.mouse-copy .view-lines,
.monaco-editor.hc-black.mac.mouse-copy .view-lines {
	cursor: copy;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Checkbox */

.monaco-checkbox .label {
	width: 12px;
	height: 12px;
	border: 1px solid black;
	background-color: transparent;
	display: inline-block;
}

.monaco-checkbox .checkbox {
	position: absolute;
	overflow: hidden;
	clip: rect(0 0 0 0);
	height: 1px;
	width: 1px;
	margin: -1px;
	padding: 0;
	border: 0;
}

.monaco-checkbox .checkbox:checked + .label {
	background-color: black;
}

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 10;
	top: -44px; /* find input height + shadow (10px) */
	height: 34px; /* find input height */
	overflow: hidden;
	line-height: 19px;

	-webkit-transition: top 200ms linear;
	-o-transition: top 200ms linear;
	-moz-transition: top 200ms linear;
	-ms-transition: top 200ms linear;
	transition: top 200ms linear;

	padding: 0 4px;
}
/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled {
	top: -74px; /* find input height + replace input height + shadow (10px) */
	height: 64px; /* find input height + replace input height */
}
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
	display: -webkit-flex;
	align-items: center;
}

.monaco-editor .find-widget.visible,
.monaco-editor .find-widget.replaceToggled.visible {
	top: 0;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	/* Style to compensate for //winjs */
	min-height: 0;
}

.monaco-editor .find-widget .replace-input .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
	display: -webkit-flex;
	align-items: center;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	height: 25px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .input {
	width: 100% !important;
	padding-right: 66px;
}
.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .input {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	display: -webkit-flex;
	flex:1;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	display: -webkit-flex;
	flex: initial;
	margin: 0 1px 0 3px;
	padding: 2px 2px 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	min-width: 20px;
	width: 20px;
	height: 20px;
	display: flex;
	display: -webkit-flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .find-widget .button:not(.disabled):hover {
	background-color: rgba(0, 0, 0, 0.1);
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 0;
	width: 18px;
	height: 100%;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .previous {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiCgkgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIKCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCIgdmlld0JveD0iLTEgLTMgMTYgMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgLTEgLTMgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cG9seWdvbiBmaWxsPSIjNDI0MjQyIiBwb2ludHM9IjEzLDQgNiw0IDksMSA2LDEgMiw1IDYsOSA5LDkgNiw2IDEzLDYgIi8+Cjwvc3ZnPgo=");
}

.monaco-editor .find-widget .next {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiCgkgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIKCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCIgdmlld0JveD0iLTEgLTMgMTYgMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgLTEgLTMgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cGF0aCBmaWxsPSIjNDI0MjQyIiBkPSJNMSw0aDdMNSwxaDNsNCw0TDgsOUg1bDMtM0gxVjR6Ii8+Cjwvc3ZnPgo=");
}

.monaco-editor .find-widget .disabled {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget .monaco-checkbox {
	width: 20px;
	height: 20px;
	display: inline-block;
	vertical-align: middle;
	margin-left: 3px;
}

.monaco-editor .find-widget .monaco-checkbox .label {
	content: '';
	display: inline-block;
	background-repeat: no-repeat;
	background-position: 0 0;
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsLTEwMzIuMzYyMikiPgogIDxyZWN0IHdpZHRoPSI5IiBoZWlnaHQ9IjIiIHg9IjIiIHk9IjEwNDYuMzYyMiIgc3R5bGU9ImZpbGw6IzQyNDI0MjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZSIgLz4KICA8cmVjdCB3aWR0aD0iMTMiIGhlaWdodD0iMiIgeD0iMiIgeT0iMTA0My4zNjIyIiBzdHlsZT0iZmlsbDojNDI0MjQyO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIiAvPgogIDxyZWN0IHdpZHRoPSI2IiBoZWlnaHQ9IjIiIHg9IjIiIHk9IjEwNDAuMzYyMiIgc3R5bGU9ImZpbGw6IzQyNDI0MjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZSIgLz4KICA8cmVjdCB3aWR0aD0iMTIiIGhlaWdodD0iMiIgeD0iMiIgeT0iMTAzNy4zNjIyIiBzdHlsZT0iZmlsbDojNDI0MjQyO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIiAvPgo8L2c+Cjwvc3ZnPg==");
	width: 20px;
	height: 20px;
	border: none;
}

.monaco-editor .find-widget .monaco-checkbox .checkbox:disabled + .label {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget .monaco-checkbox .checkbox:not(:disabled) + .label {
	cursor: pointer;
}

.monaco-editor .find-widget .monaco-checkbox .checkbox:not(:disabled):hover:before + .label {
	background-color: #DDD;
}

.monaco-editor .find-widget .monaco-checkbox .checkbox:checked + .label {
	background-color: rgba(100, 100, 100, 0.2);
}

.monaco-editor .find-widget .close-fw {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iIzQyNDI0MiIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==");
}

.monaco-editor .find-widget .expand {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iIzY0NjQ2NSIgZD0iTTExIDEwLjA3aC01LjY1Nmw1LjY1Ni01LjY1NnY1LjY1NnoiLz48L3N2Zz4=");
}

.monaco-editor .find-widget .collapse {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iIzY0NjQ2NSIgZD0iTTYgNHY4bDQtNC00LTR6bTEgMi40MTRsMS41ODYgMS41ODYtMS41ODYgMS41ODZ2LTMuMTcyeiIvPjwvc3ZnPg==");
}

.monaco-editor .find-widget .replace {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTZweCIKCSBoZWlnaHQ9IjE2cHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8ZyBpZD0iaWNvbl94NUZfYmciPgoJPGc+CgkJPHBhdGggZmlsbD0iIzQyNDI0MiIgZD0iTTExLDNWMWgtMXY1djFoMWgyaDFWNFYzSDExeiBNMTMsNmgtMlY0aDJWNnoiLz4KCQk8cGF0aCBmaWxsPSIjNDI0MjQyIiBkPSJNMiwxNWg3VjlIMlYxNXogTTQsMTBoM3YxSDV2MmgydjFINFYxMHoiLz4KCTwvZz4KPC9nPgo8ZyBpZD0iY29sb3JfeDVGX2ltcG9ydGFuY2UiPgoJPHBhdGggZmlsbD0iIzAwNTM5QyIgZD0iTTMuOTc5LDMuNUw0LDZMMyw1djEuNUw0LjUsOEw2LDYuNVY1TDUsNkw0Ljk3OSwzLjVjMC0wLjI3NSwwLjIyNS0wLjUsMC41LTAuNUg5VjJINS40NzkKCQlDNC42NTEsMiwzLjk3OSwyLjY3MywzLjk3OSwzLjV6Ii8+CjwvZz4KPC9zdmc+Cg==");
}

.monaco-editor .find-widget .replace-all {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTZweCIKCSBoZWlnaHQ9IjE2cHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8ZyBpZD0iaWNvbl94NUZfYmciPgoJPHBhdGggZmlsbD0iIzQyNDI0MiIgZD0iTTExLDE1VjlIMXY2SDExeiBNMiwxNHYtMmgxdi0xSDJ2LTFoM3Y0SDJ6IE0xMCwxMUg4djJoMnYxSDd2LTRoM1YxMXogTTMsMTN2LTFoMXYxSDN6IE0xMyw3djZoLTFWOEg1VjcKCQlIMTN6IE0xMywyVjFoLTF2NWgzVjJIMTN6IE0xNCw1aC0xVjNoMVY1eiBNMTEsMnY0SDhWNGgxdjFoMVY0SDlWM0g4VjJIMTF6Ii8+CjwvZz4KPGcgaWQ9ImNvbG9yX3g1Rl9hY3Rpb24iPgoJPHBhdGggZmlsbD0iIzAwNTM5QyIgZD0iTTEuOTc5LDMuNUwyLDZMMSw1djEuNUwyLjUsOEw0LDYuNVY1TDMsNkwyLjk3OSwzLjVjMC0wLjI3NSwwLjIyNS0wLjUsMC41LTAuNUg3VjJIMy40NzkKCQlDMi42NTEsMiwxLjk3OSwyLjY3MywxLjk3OSwzLjV6Ii8+CjwvZz4KPC9zdmc+Cg==");
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .replace-input {
	display: flex;
	display: -webkit-flex;
	vertical-align: middle;
	width: auto !important;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount,
.monaco-editor .find-widget.reduced-find-widget .monaco-checkbox {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 111px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-inputbox > .wrapper > .input {
	padding-right: 0px;
}

.monaco-editor .findMatch {
	-webkit-animation-duration: 0;
	-webkit-animation-name: inherit !important;
	-moz-animation-duration: 0;
	-moz-animation-name: inherit !important;
	-ms-animation-duration: 0;
	-ms-animation-name: inherit !important;
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	width: 2px !important;
	margin-left: -4px;
}

.monaco-editor.hc-black .find-widget .previous,
.monaco-editor.vs-dark .find-widget .previous {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiCgkgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIKCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCIgdmlld0JveD0iLTEgLTMgMTYgMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgLTEgLTMgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cG9seWdvbiBmaWxsPSIjQzVDNUM1IiBwb2ludHM9IjEzLDQgNiw0IDksMSA2LDEgMiw1IDYsOSA5LDkgNiw2IDEzLDYgIi8+Cjwvc3ZnPgo=");
}

.monaco-editor.hc-black .find-widget .next,
.monaco-editor.vs-dark .find-widget .next {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiCgkgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIKCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCIgdmlld0JveD0iLTEgLTMgMTYgMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgLTEgLTMgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cGF0aCBmaWxsPSIjQzVDNUM1IiBkPSJNMSw0aDdMNSwxaDNsNCw0TDgsOUg1bDMtM0gxVjR6Ii8+Cjwvc3ZnPgo=");
}

.monaco-editor.hc-black .find-widget .monaco-checkbox .label,
.monaco-editor.vs-dark .find-widget .monaco-checkbox .label {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsLTEwMzIuMzYyMikiPgogIDxyZWN0IHdpZHRoPSI5IiBoZWlnaHQ9IjIiIHg9IjIiIHk9IjEwNDYuMzYyMiIgc3R5bGU9ImZpbGw6I0M1QzVDNTtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZSIgLz4KICA8cmVjdCB3aWR0aD0iMTMiIGhlaWdodD0iMiIgeD0iMiIgeT0iMTA0My4zNjIyIiBzdHlsZT0iZmlsbDojQzVDNUM1O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIiAvPgogIDxyZWN0IHdpZHRoPSI2IiBoZWlnaHQ9IjIiIHg9IjIiIHk9IjEwNDAuMzYyMiIgc3R5bGU9ImZpbGw6I0M1QzVDNTtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZSIgLz4KICA8cmVjdCB3aWR0aD0iMTIiIGhlaWdodD0iMiIgeD0iMiIgeT0iMTAzNy4zNjIyIiBzdHlsZT0iZmlsbDojQzVDNUM1O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIiAvPgo8L2c+Cjwvc3ZnPg==");
}

.monaco-editor.vs-dark .find-widget .monaco-checkbox .checkbox:not(:disabled):hover:before + .label {
	background-color: rgba(255, 255, 255, 0.1);
}

.monaco-editor.vs-dark .find-widget .monaco-checkbox .checkbox:checked + .label {
	background-color: rgba(255, 255, 255, 0.1);
}

.monaco-editor.hc-black .find-widget .close-fw,
.monaco-editor.vs-dark .find-widget .close-fw {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iI2U4ZThlOCIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==");
}

.monaco-editor.hc-black .find-widget .replace,
.monaco-editor.vs-dark .find-widget .replace {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTZweCIKCSBoZWlnaHQ9IjE2cHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8ZyBpZD0iaWNvbl94NUZfYmciPgoJPGc+CgkJPHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTExLDNWMWgtMXY1djFoMWgyaDFWNFYzSDExeiBNMTMsNmgtMlY0aDJWNnoiLz4KCQk8cGF0aCBmaWxsPSIjQzVDNUM1IiBkPSJNMiwxNWg3VjlIMlYxNXogTTQsMTBoM3YxSDV2MmgydjFINFYxMHoiLz4KCTwvZz4KPC9nPgo8ZyBpZD0iY29sb3JfeDVGX2ltcG9ydGFuY2UiPgoJPHBhdGggZmlsbD0iIzc1QkVGRiIgZD0iTTMuOTc5LDMuNUw0LDZMMyw1djEuNUw0LjUsOEw2LDYuNVY1TDUsNkw0Ljk3OSwzLjVjMC0wLjI3NSwwLjIyNS0wLjUsMC41LTAuNUg5VjJINS40NzkKCQlDNC42NTEsMiwzLjk3OSwyLjY3MywzLjk3OSwzLjV6Ii8+CjwvZz4KPC9zdmc+Cg==");
}

.monaco-editor.hc-black .find-widget .replace-all,
.monaco-editor.vs-dark .find-widget .replace-all {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTZweCIKCSBoZWlnaHQ9IjE2cHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8ZyBpZD0iaWNvbl94NUZfYmciPgoJPHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTExLDE1VjlIMXY2SDExeiBNMiwxNHYtMmgxdi0xSDJ2LTFoM3Y0SDJ6IE0xMCwxMUg4djJoMnYxSDd2LTRoM1YxMXogTTMsMTN2LTFoMXYxSDN6IE0xMyw3djZoLTFWOEg1VjcKCQlIMTN6IE0xMywyVjFoLTF2NWgzVjJIMTN6IE0xNCw1aC0xVjNoMVY1eiBNMTEsMnY0SDhWNGgxdjFoMVY0SDlWM0g4VjJIMTF6Ii8+CjwvZz4KPGcgaWQ9ImNvbG9yX3g1Rl9hY3Rpb24iPgoJPHBhdGggZmlsbD0iIzc1QkVGRiIgZD0iTTEuOTc5LDMuNUwyLDZMMSw1djEuNUwyLjUsOEw0LDYuNVY1TDMsNkwyLjk3OSwzLjVjMC0wLjI3NSwwLjIyNS0wLjUsMC41LTAuNUg3VjJIMy40NzkKCQlDMi42NTEsMiwxLjk3OSwyLjY3MywxLjk3OSwzLjV6Ii8+CjwvZz4KPC9zdmc+Cg==");
}

.monaco-editor.hc-black .find-widget .expand,
.monaco-editor.vs-dark .find-widget .expand {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI2U4ZThlOCIgZD0iTTExIDEwLjA3aC01LjY1Nmw1LjY1Ni01LjY1NnY1LjY1NnoiLz48L3N2Zz4=");
}

.monaco-editor.hc-black .find-widget .collapse,
.monaco-editor.vs-dark .find-widget .collapse {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI2U4ZThlOCIgZD0iTTYgNHY4bDQtNC00LTR6bTEgMi40MTRsMS41ODYgMS41ODYtMS41ODYgMS41ODZ2LTMuMTcyeiIvPjwvc3ZnPg==");
}

.monaco-editor.hc-black .find-widget .button:not(.disabled):hover,
.monaco-editor.vs-dark .find-widget .button:not(.disabled):hover {
	background-color: rgba(255, 255, 255, 0.1);
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}

.monaco-editor.hc-black .find-widget .monaco-checkbox .checkbox:checked + .label {
	background-color: rgba(255, 255, 255, 0.1);
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
	height: 25px;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}
.monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	line-height: auto !important;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .wrapper > .input,
.monaco-inputbox > .wrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .wrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .wrapper > .input {
	display: inline-block;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .wrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .wrapper > textarea.input {
	display: block;
	overflow: hidden;
}

.monaco-inputbox > .wrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	white-space: pre-wrap;
	visibility: hidden;
	min-height: 26px;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	min-height: 34px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .icon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.vs .monaco-custom-checkbox.monaco-case-sensitive {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3Qwe29wYWNpdHk6MDtmaWxsOiNGNkY2RjY7fSAuc3Qxe2ZpbGw6I0Y2RjZGNjt9IC5zdDJ7ZmlsbDojNDI0MjQyO308L3N0eWxlPjxnIGlkPSJvdXRsaW5lIj48cmVjdCBjbGFzcz0ic3QwIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiLz48cGF0aCBjbGFzcz0ic3QxIiBkPSJNMTQuMTc2IDUuNTkyYy0uNTU1LS42LTEuMzM2LS45MDQtMi4zMjItLjkwNC0uMjU4IDAtLjUyMS4wMjQtLjc4NC4wNzItLjI0Ni4wNDQtLjQ3OS4xMDEtLjcuMTY5LS4yMjguMDctLjQzMi4xNDctLjYxMy4yMjktLjIyLjA5OS0uMzg5LjE5Ni0uNTEyLjI4NGwtLjQxOS4yOTl2Mi43MDFjLS4wODYuMTA4LS4xNjIuMjIzLS4yMjkuMzQ0bC0yLjQ1LTYuMzU0aC0yLjM5NGwtMy43NTMgOS44MDR2LjU5OGgzLjAyNWwuODM4LTIuMzVoMi4xNjdsLjg5MSAyLjM1aDMuMjM3bC0uMDAxLS4wMDNjLjMwNS4wOTIuNjMzLjE1Ljk5My4xNS4zNDQgMCAuNjcxLS4wNDkuOTc4LS4xNDZoMi44NTN2LTQuOTAzYy0uMDAxLS45NzUtLjI3MS0xLjc2My0uODA1LTIuMzR6Ii8+PC9nPjxnIGlkPSJpY29uX3g1Rl9iZyI+PHBhdGggY2xhc3M9InN0MiIgZD0iTTcuNjExIDExLjgzNGwtLjg5MS0yLjM1aC0zLjU2MmwtLjgzOCAyLjM1aC0xLjA5NWwzLjIxNy04LjQwMmgxLjAybDMuMjQgOC40MDJoLTEuMDkxem0tMi41MzEtNi44MTRsLS4wNDQtLjEzNS0uMDM4LS4xNTYtLjAyOS0uMTUyLS4wMjQtLjEyNmgtLjAyM2wtLjAyMS4xMjYtLjAzMi4xNTItLjAzOC4xNTYtLjA0NC4xMzUtMS4zMDcgMy41NzRoMi45MThsLTEuMzE4LTMuNTc0eiIvPjxwYXRoIGNsYXNzPSJzdDIiIGQ9Ik0xMy4wMiAxMS44MzR2LS45MzhoLS4wMjNjLS4xOTkuMzUyLS40NTYuNjItLjc3MS44MDZzLS42NzMuMjc4LTEuMDc1LjI3OGMtLjMxMyAwLS41ODgtLjA0NS0uODI2LS4xMzVzLS40MzgtLjIxMi0uNTk4LS4zNjYtLjI4MS0uMzM4LS4zNjMtLjU1MS0uMTI0LS40NDItLjEyNC0uNjg4YzAtLjI2Mi4wMzktLjUwMi4xMTctLjcyMXMuMTk4LS40MTIuMzYtLjU4LjM2Ny0uMzA4LjYxNS0uNDE5LjU0NC0uMTkuODg4LS4yMzdsMS44MTEtLjI1MmMwLS4yNzMtLjAyOS0uNTA3LS4wODgtLjdzLS4xNDMtLjM1MS0uMjUyLS40NzItLjI0MS0uMjEtLjM5Ni0uMjY3LS4zMjUtLjA4NS0uNTEzLS4wODVjLS4zNjMgMC0uNzE0LjA2NC0xLjA1Mi4xOTNzLS42MzguMzEtLjkwNC41NHYtLjk4NGMuMDgyLS4wNTkuMTk2LS4xMjEuMzQzLS4xODhzLjMxMi0uMTI4LjQ5NS0uMTg1LjM3OC0uMTA0LjU4My0uMTQxLjQwNy0uMDU2LjYwNi0uMDU2Yy42OTkgMCAxLjIyOS4xOTQgMS41ODguNTgzcy41MzkuOTQyLjUzOSAxLjY2MXYzLjkwMmgtLjk2em0tMS40NTQtMi44M2MtLjI3My4wMzUtLjQ5OC4wODUtLjY3NC4xNDlzLS4zMTMuMTQ0LS40MS4yMzctLjE2NS4yMDUtLjIwMi4zMzQtLjA1NS4yNzYtLjA1NS40NGMwIC4xNDEuMDI1LjI3MS4wNzYuMzkzcy4xMjQuMjI3LjIyLjMxNi4yMTUuMTYuMzU3LjIxMS4zMDguMDc2LjQ5NS4wNzZjLjI0MiAwIC40NjUtLjA0NS42NjgtLjEzNXMuMzc4LS4yMTQuNTI0LS4zNzIuMjYxLS4zNDQuMzQzLS41NTcuMTIzLS40NDIuMTIzLS42ODh2LS42MDlsLTEuNDY1LjIwNXoiLz48L2c+PC9zdmc+") center center no-repeat;
}
.hc-black .monaco-custom-checkbox.monaco-case-sensitive,
.hc-black .monaco-custom-checkbox.monaco-case-sensitive:hover,
.vs-dark .monaco-custom-checkbox.monaco-case-sensitive {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3Qwe29wYWNpdHk6MDtmaWxsOiMyNjI2MjY7fSAuc3Qxe2ZpbGw6IzI2MjYyNjt9IC5zdDJ7ZmlsbDojQzVDNUM1O308L3N0eWxlPjxnIGlkPSJvdXRsaW5lIj48cmVjdCBjbGFzcz0ic3QwIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiLz48cGF0aCBjbGFzcz0ic3QxIiBkPSJNMTQuMTc2IDUuNTkyYy0uNTU1LS42LTEuMzM2LS45MDQtMi4zMjItLjkwNC0uMjU4IDAtLjUyMS4wMjQtLjc4NC4wNzItLjI0Ni4wNDQtLjQ3OS4xMDEtLjcuMTY5LS4yMjguMDctLjQzMi4xNDctLjYxMy4yMjktLjIyLjA5OS0uMzg5LjE5Ni0uNTEyLjI4NGwtLjQxOS4yOTl2Mi43MDFjLS4wODYuMTA4LS4xNjIuMjIzLS4yMjkuMzQ0bC0yLjQ1LTYuMzU0aC0yLjM5NGwtMy43NTMgOS44MDR2LjU5OGgzLjAyNWwuODM4LTIuMzVoMi4xNjdsLjg5MSAyLjM1aDMuMjM3bC0uMDAxLS4wMDNjLjMwNS4wOTIuNjMzLjE1Ljk5My4xNS4zNDQgMCAuNjcxLS4wNDkuOTc4LS4xNDZoMi44NTN2LTQuOTAzYy0uMDAxLS45NzUtLjI3MS0xLjc2My0uODA1LTIuMzR6Ii8+PC9nPjxnIGlkPSJpY29uX3g1Rl9iZyI+PHBhdGggY2xhc3M9InN0MiIgZD0iTTcuNjExIDExLjgzNGwtLjg5MS0yLjM1aC0zLjU2MmwtLjgzOCAyLjM1aC0xLjA5NWwzLjIxNy04LjQwMmgxLjAybDMuMjQgOC40MDJoLTEuMDkxem0tMi41MzEtNi44MTRsLS4wNDQtLjEzNS0uMDM4LS4xNTYtLjAyOS0uMTUyLS4wMjQtLjEyNmgtLjAyM2wtLjAyMS4xMjYtLjAzMi4xNTItLjAzOC4xNTYtLjA0NC4xMzUtMS4zMDcgMy41NzRoMi45MThsLTEuMzE4LTMuNTc0eiIvPjxwYXRoIGNsYXNzPSJzdDIiIGQ9Ik0xMy4wMiAxMS44MzR2LS45MzhoLS4wMjNjLS4xOTkuMzUyLS40NTYuNjItLjc3MS44MDZzLS42NzMuMjc4LTEuMDc1LjI3OGMtLjMxMyAwLS41ODgtLjA0NS0uODI2LS4xMzVzLS40MzgtLjIxMi0uNTk4LS4zNjYtLjI4MS0uMzM4LS4zNjMtLjU1MS0uMTI0LS40NDItLjEyNC0uNjg4YzAtLjI2Mi4wMzktLjUwMi4xMTctLjcyMXMuMTk4LS40MTIuMzYtLjU4LjM2Ny0uMzA4LjYxNS0uNDE5LjU0NC0uMTkuODg4LS4yMzdsMS44MTEtLjI1MmMwLS4yNzMtLjAyOS0uNTA3LS4wODgtLjdzLS4xNDMtLjM1MS0uMjUyLS40NzItLjI0MS0uMjEtLjM5Ni0uMjY3LS4zMjUtLjA4NS0uNTEzLS4wODVjLS4zNjMgMC0uNzE0LjA2NC0xLjA1Mi4xOTNzLS42MzguMzEtLjkwNC41NHYtLjk4NGMuMDgyLS4wNTkuMTk2LS4xMjEuMzQzLS4xODhzLjMxMi0uMTI4LjQ5NS0uMTg1LjM3OC0uMTA0LjU4My0uMTQxLjQwNy0uMDU2LjYwNi0uMDU2Yy42OTkgMCAxLjIyOS4xOTQgMS41ODguNTgzcy41MzkuOTQyLjUzOSAxLjY2MXYzLjkwMmgtLjk2em0tMS40NTQtMi44M2MtLjI3My4wMzUtLjQ5OC4wODUtLjY3NC4xNDlzLS4zMTMuMTQ0LS40MS4yMzctLjE2NS4yMDUtLjIwMi4zMzQtLjA1NS4yNzYtLjA1NS40NGMwIC4xNDEuMDI1LjI3MS4wNzYuMzkzcy4xMjQuMjI3LjIyLjMxNi4yMTUuMTYuMzU3LjIxMS4zMDguMDc2LjQ5NS4wNzZjLjI0MiAwIC40NjUtLjA0NS42NjgtLjEzNXMuMzc4LS4yMTQuNTI0LS4zNzIuMjYxLS4zNDQuMzQzLS41NTcuMTIzLS40NDIuMTIzLS42ODh2LS42MDlsLTEuNDY1LjIwNXoiLz48L2c+PC9zdmc+") center center no-repeat;
}

.vs .monaco-custom-checkbox.monaco-whole-word {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3Qwe29wYWNpdHk6MDtmaWxsOiNGNkY2RjY7fSAuc3Qxe2ZpbGw6I0Y2RjZGNjt9IC5zdDJ7ZmlsbDojNDI0MjQyO308L3N0eWxlPjxnIGlkPSJvdXRsaW5lIj48cmVjdCBjbGFzcz0ic3QwIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiLz48cGF0aCBjbGFzcz0ic3QxIiBkPSJNMTYgNC4wMjJ2LTMuMDIyaC0xNi4wMTR2My4wMjJoMy4wNDZsLTMuMDQzIDcuOTQ1aC0uMDA0di4wMWwuMDE1IDEuMDIzaC0uMDE0djEuOTkxaDE2LjAxNHYtMy4wMjNoLTF2LTcuOTQ2aDF6bS01LjkxNCA1LjMwMWMwIC4yMzMtLjAyMy40NDEtLjA2Ni41OTUtLjA0Ny4xNjQtLjA5OS4yNDctLjEyNy4yODRsLS4wNzguMDY5LS4xNTEuMDI2LS4xMTUtLjAxNy0uMTM5LS4xMzdjLS4wMzEtLjA3OC0uMTEyLS4zMzItLjExMi0uNTY2IDAtLjI1NC4wOTEtLjU2MS4xMjYtLjY1NmwuMDY5LS4xNDEuMTA5LS4wODIuMTc4LS4wMjdjLjA3NyAwIC4xMTcuMDE0LjE3Ny4wNTZsLjA4Ny4xNzkuMDUxLjIzNy0uMDA5LjE4em0tMy42OTUtNS4zMDF2Mi44OTNsLTEuMTE2LTIuODkzaDEuMTE2em0tMy4wMjYgNy4wMmgxLjU3M2wuMzUxLjkyNmgtMi4yNTRsLjMzLS45MjZ6bTguNjM1LTQuMzU0Yy0uMjA2LS4yLS40MzEtLjM4LS42OTUtLjUxMi0uMzk2LS4xOTgtLjg1My0uMjk4LTEuMzU1LS4yOTgtLjIxNSAwLS40MjMuMDItLjYyMS4wNTh2LTEuOTE0aDIuNjcxdjIuNjY2eiIvPjwvZz48ZyBpZD0iaWNvbl94NUZfYmciPjxyZWN0IHg9IjEzIiB5PSI0IiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+PHBhdGggY2xhc3M9InN0MiIgZD0iTTExLjIyNSA4LjM4N2MtLjA3OC0uMjk5LS4xOTktLjU2Mi0uMzYtLjc4NnMtLjM2NS0uNDAxLS42MDktLjUzLS41MzQtLjE5My0uODY2LS4xOTNjLS4xOTggMC0uMzguMDI0LS41NDcuMDczLS4xNjUuMDQ5LS4zMTYuMTE3LS40NTMuMjA1LS4xMzYuMDg4LS4yNTcuMTk0LS4zNjUuMzE4bC0uMTc5LjI1OHYtMy4xNTRoLS44OTN2Ny40MjJoLjg5M3YtLjU3NWwuMTI2LjE3NWMuMDg3LjEwMi4xODkuMTkuMzA0LjI2OS4xMTcuMDc4LjI0OS4xNC4zOTguMTg2LjE0OS4wNDYuMzE0LjA2OC40OTguMDY4LjM1MyAwIC42NjYtLjA3MS45MzctLjIxMi4yNzItLjE0My40OTktLjMzOC42ODItLjU4Ni4xODMtLjI1LjMyMS0uNTQzLjQxNC0uODc5LjA5My0uMzM4LjE0LS43MDMuMTQtMS4wOTctLjAwMS0uMzQyLS4wNC0uNjYzLS4xMi0uOTYyem0tMS40NzktLjYwN2MuMTUxLjA3MS4yODIuMTc2LjM5LjMxNC4xMDkuMTQuMTk0LjMxMy4yNTUuNTE3LjA1MS4xNzQuMDgyLjM3MS4wODkuNTg3bC0uMDA3LjEyNWMwIC4zMjctLjAzMy42Mi0uMS44NjktLjA2Ny4yNDYtLjE2MS40NTMtLjI3OC42MTQtLjExNy4xNjItLjI2LjI4NS0uNDIxLjM2Ni0uMzIyLjE2Mi0uNzYuMTY2LTEuMDY5LjAxNS0uMTUzLS4wNzUtLjI4Ni0uMTc1LS4zOTMtLjI5Ni0uMDg1LS4wOTYtLjE1Ni0uMjE2LS4yMTgtLjM2NyAwIDAtLjE3OS0uNDQ3LS4xNzktLjk0NyAwLS41LjE3OS0xLjAwMi4xNzktMS4wMDIuMDYyLS4xNzcuMTM2LS4zMTguMjI0LS40My4xMTQtLjE0My4yNTYtLjI1OS40MjQtLjM0NS4xNjgtLjA4Ni4zNjUtLjEyOS41ODctLjEyOS4xOSAwIC4zNjQuMDM3LjUxNy4xMDl6Ii8+PHJlY3QgeD0iLjk4NyIgeT0iMiIgY2xhc3M9InN0MiIgd2lkdGg9IjE0LjAxMyIgaGVpZ2h0PSIxLjAyMyIvPjxyZWN0IHg9Ii45ODciIHk9IjEyLjk2OCIgY2xhc3M9InN0MiIgd2lkdGg9IjE0LjAxMyIgaGVpZ2h0PSIxLjAyMyIvPjxwYXRoIGNsYXNzPSJzdDIiIGQ9Ik0xLjk5MSAxMi4wMzFsLjcyOC0yLjAzMWgyLjIxOWwuNzc4IDIuMDMxaDEuMDgybC0yLjQ4NS03LjE1OGgtLjk0MWwtMi40NDEgNy4wODYtLjAyNS4wNzJoMS4wODV6bTEuODI3LTUuNjA5aC4wMjJsLjkxNCAyLjc1M2gtMS44NDFsLjkwNS0yLjc1M3oiLz48L2c+PC9zdmc+") center center no-repeat;
}
.hc-black .monaco-custom-checkbox.monaco-whole-word,
.hc-black .monaco-custom-checkbox.monaco-whole-word:hover,
.vs-dark .monaco-custom-checkbox.monaco-whole-word {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3Qwe29wYWNpdHk6MDtmaWxsOiMyNjI2MjY7fSAuc3Qxe2ZpbGw6IzI2MjYyNjt9IC5zdDJ7ZmlsbDojQzVDNUM1O308L3N0eWxlPjxnIGlkPSJvdXRsaW5lIj48cmVjdCBjbGFzcz0ic3QwIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiLz48cGF0aCBjbGFzcz0ic3QxIiBkPSJNMTYgNC4wMjJ2LTMuMDIyaC0xNi4wMTR2My4wMjJoMy4wNDZsLTMuMDQzIDcuOTQ1aC0uMDA0di4wMWwuMDE1IDEuMDIzaC0uMDE0djEuOTkxaDE2LjAxNHYtMy4wMjNoLTF2LTcuOTQ2aDF6bS01LjkxNCA1LjMwMWMwIC4yMzMtLjAyMy40NDEtLjA2Ni41OTUtLjA0Ny4xNjQtLjA5OS4yNDctLjEyNy4yODRsLS4wNzguMDY5LS4xNTEuMDI2LS4xMTUtLjAxNy0uMTM5LS4xMzdjLS4wMzEtLjA3OC0uMTEyLS4zMzItLjExMi0uNTY2IDAtLjI1NC4wOTEtLjU2MS4xMjYtLjY1NmwuMDY5LS4xNDEuMTA5LS4wODIuMTc4LS4wMjdjLjA3NyAwIC4xMTcuMDE0LjE3Ny4wNTZsLjA4Ny4xNzkuMDUxLjIzNy0uMDA5LjE4em0tMy42OTUtNS4zMDF2Mi44OTNsLTEuMTE2LTIuODkzaDEuMTE2em0tMy4wMjYgNy4wMmgxLjU3M2wuMzUxLjkyNmgtMi4yNTRsLjMzLS45MjZ6bTguNjM1LTQuMzU0Yy0uMjA2LS4yLS40MzEtLjM4LS42OTUtLjUxMi0uMzk2LS4xOTgtLjg1My0uMjk4LTEuMzU1LS4yOTgtLjIxNSAwLS40MjMuMDItLjYyMS4wNTh2LTEuOTE0aDIuNjcxdjIuNjY2eiIvPjwvZz48ZyBpZD0iaWNvbl94NUZfYmciPjxyZWN0IHg9IjEzIiB5PSI0IiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+PHBhdGggY2xhc3M9InN0MiIgZD0iTTExLjIyNSA4LjM4N2MtLjA3OC0uMjk5LS4xOTktLjU2Mi0uMzYtLjc4NnMtLjM2NS0uNDAxLS42MDktLjUzLS41MzQtLjE5My0uODY2LS4xOTNjLS4xOTggMC0uMzguMDI0LS41NDcuMDczLS4xNjUuMDQ5LS4zMTYuMTE3LS40NTMuMjA1LS4xMzYuMDg4LS4yNTcuMTk0LS4zNjUuMzE4bC0uMTc5LjI1OHYtMy4xNTRoLS44OTN2Ny40MjJoLjg5M3YtLjU3NWwuMTI2LjE3NWMuMDg3LjEwMi4xODkuMTkuMzA0LjI2OS4xMTcuMDc4LjI0OS4xNC4zOTguMTg2LjE0OS4wNDYuMzE0LjA2OC40OTguMDY4LjM1MyAwIC42NjYtLjA3MS45MzctLjIxMi4yNzItLjE0My40OTktLjMzOC42ODItLjU4Ni4xODMtLjI1LjMyMS0uNTQzLjQxNC0uODc5LjA5My0uMzM4LjE0LS43MDMuMTQtMS4wOTctLjAwMS0uMzQyLS4wNC0uNjYzLS4xMi0uOTYyem0tMS40NzktLjYwN2MuMTUxLjA3MS4yODIuMTc2LjM5LjMxNC4xMDkuMTQuMTk0LjMxMy4yNTUuNTE3LjA1MS4xNzQuMDgyLjM3MS4wODkuNTg3bC0uMDA3LjEyNWMwIC4zMjctLjAzMy42Mi0uMS44NjktLjA2Ny4yNDYtLjE2MS40NTMtLjI3OC42MTQtLjExNy4xNjItLjI2LjI4NS0uNDIxLjM2Ni0uMzIyLjE2Mi0uNzYuMTY2LTEuMDY5LjAxNS0uMTUzLS4wNzUtLjI4Ni0uMTc1LS4zOTMtLjI5Ni0uMDg1LS4wOTYtLjE1Ni0uMjE2LS4yMTgtLjM2NyAwIDAtLjE3OS0uNDQ3LS4xNzktLjk0NyAwLS41LjE3OS0xLjAwMi4xNzktMS4wMDIuMDYyLS4xNzcuMTM2LS4zMTguMjI0LS40My4xMTQtLjE0My4yNTYtLjI1OS40MjQtLjM0NS4xNjgtLjA4Ni4zNjUtLjEyOS41ODctLjEyOS4xOSAwIC4zNjQuMDM3LjUxNy4xMDl6Ii8+PHJlY3QgeD0iLjk4NyIgeT0iMiIgY2xhc3M9InN0MiIgd2lkdGg9IjE0LjAxMyIgaGVpZ2h0PSIxLjAyMyIvPjxyZWN0IHg9Ii45ODciIHk9IjEyLjk2OCIgY2xhc3M9InN0MiIgd2lkdGg9IjE0LjAxMyIgaGVpZ2h0PSIxLjAyMyIvPjxwYXRoIGNsYXNzPSJzdDIiIGQ9Ik0xLjk5MSAxMi4wMzFsLjcyOC0yLjAzMWgyLjIxOWwuNzc4IDIuMDMxaDEuMDgybC0yLjQ4NS03LjE1OGgtLjk0MWwtMi40NDEgNy4wODYtLjAyNS4wNzJoMS4wODV6bTEuODI3LTUuNjA5aC4wMjJsLjkxNCAyLjc1M2gtMS44NDFsLjkwNS0yLjc1M3oiLz48L2c+PC9zdmc+") center center no-repeat;
}

.vs .monaco-custom-checkbox.monaco-regex {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBvbHlnb24gZmlsbD0iI0Y2RjZGNiIgcG9pbnRzPSIxMy42NCw3LjM5NiAxMi4xNjksMi44OTggMTAuNzA2LDMuNzYxIDExLjA4NywyIDYuNTU3LDIgNi45MzYsMy43NjIgNS40NzMsMi44OTggNCw3LjM5NiA1LjY4Miw3LjU1NCA0LjUxMyw4LjU2MSA1LjAxMyw5IDIsOSAyLDE0IDcsMTQgNywxMC43NDcgNy45NzgsMTEuNjA2IDguODIsOS43MjUgOS42NjEsMTEuNjAyIDEzLjE0NCw4LjU2MiAxMS45NjgsNy41NTQiLz48ZyBmaWxsPSIjNDI0MjQyIj48cGF0aCBkPSJNMTIuMzAxIDYuNTE4bC0yLjc3Mi4yNjIgMi4wODYgMS43ODgtMS41OTQgMS4zOTItMS4yMDEtMi42ODItMS4yMDEgMi42ODItMS41ODMtMS4zOTIgMi4wNzUtMS43ODgtMi43NzEtLjI2Mi42OTYtMi4xMjYgMi4zNTggMS4zOTItLjU5OS0yLjc4NGgyLjA1M2wtLjYwMiAyLjc4MyAyLjM1OS0xLjM5Mi42OTYgMi4xMjd6Ii8+PHJlY3QgeD0iMyIgeT0iMTAiIHdpZHRoPSIzIiBoZWlnaHQ9IjMiLz48L2c+PC9zdmc+") center center no-repeat;
}
.hc-black .monaco-custom-checkbox.monaco-regex,
.hc-black .monaco-custom-checkbox.monaco-regex:hover,
.vs-dark .monaco-custom-checkbox.monaco-regex {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBvbHlnb24gZmlsbD0iIzJkMmQzMCIgcG9pbnRzPSIxMy42NCw3LjM5NiAxMi4xNjksMi44OTggMTAuNzA2LDMuNzYxIDExLjA4NywyIDYuNTU3LDIgNi45MzYsMy43NjIgNS40NzMsMi44OTggNCw3LjM5NiA1LjY4Miw3LjU1NCA0LjUxMyw4LjU2MSA1LjAxMyw5IDIsOSAyLDE0IDcsMTQgNywxMC43NDcgNy45NzgsMTEuNjA2IDguODIsOS43MjUgOS42NjEsMTEuNjAyIDEzLjE0NCw4LjU2MiAxMS45NjgsNy41NTQiLz48ZyBmaWxsPSIjQzVDNUM1Ij48cGF0aCBkPSJNMTIuMzAxIDYuNTE4bC0yLjc3Mi4yNjIgMi4wODYgMS43ODgtMS41OTQgMS4zOTItMS4yMDEtMi42ODItMS4yMDEgMi42ODItMS41ODMtMS4zOTIgMi4wNzUtMS43ODgtMi43NzEtLjI2Mi42OTYtMi4xMjYgMi4zNTggMS4zOTItLjU5OS0yLjc4NGgyLjA1M2wtLjYwMiAyLjc4MyAyLjM1OS0xLjM5Mi42OTYgMi4xMjd6Ii8+PHJlY3QgeD0iMyIgeT0iMTAiIHdpZHRoPSIzIiBoZWlnaHQ9IjMiLz48L2c+PC9zdmc+") center center no-repeat;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-checkbox {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	opacity: 0.7;
	width: 20px;
	height: 20px;
	border: 1px solid transparent;
	padding: 1px;

	-webkit-box-sizing:	border-box;
	-o-box-sizing:		border-box;
	-moz-box-sizing:	border-box;
	-ms-box-sizing:		border-box;
	box-sizing:			border-box;

	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-o-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.monaco-custom-checkbox:hover,
.monaco-custom-checkbox.checked {
	opacity: 1;
}

.hc-black .monaco-custom-checkbox {
	background: none;
}

.hc-black .monaco-custom-checkbox:hover {
	background: none;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .folding {
	margin-left: 5px;
	cursor: pointer;
	background-repeat: no-repeat;
	background-origin: border-box;
	background-position: 3px center;
	background-size: 15px;
	opacity: 0;
	transition: opacity 0.5s;
}

.monaco-editor .margin-view-overlays .folding {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTUgMTUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDE1IDE1OyI+CjxwYXRoIHN0eWxlPSJmaWxsOiNCNkI2QjYiIGQ9Ik0xMSw0djdINFY0SDExIE0xMiwzSDN2OWg5VjNMMTIsM3oiLz4KPGxpbmUgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6IzZCNkI2QjtzdHJva2UtbWl0ZXJsaW1pdDoxMCIgeDE9IjEwIiB5MT0iNy41IiB4Mj0iNSIgeTI9IjcuNSIvPgo8L3N2Zz4=");
}

.monaco-editor.hc-black .margin-view-overlays .folding,
.monaco-editor.vs-dark .margin-view-overlays .folding {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTUgMTUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDE1IDE1OyI+CjxwYXRoIHN0eWxlPSJmaWxsOiM1QTVBNUEiIGQ9Ik0xMSw0djdINFY0SDExIE0xMiwzSDN2OWg5VjNMMTIsM3oiLz4KPGxpbmUgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6I0M1QzVDNTtzdHJva2UtbWl0ZXJsaW1pdDoxMCIgeDE9IjEwIiB5MT0iNy41IiB4Mj0iNSIgeTI9IjcuNSIvPgo8L3N2Zz4=");
}

.monaco-editor .margin-view-overlays:hover .folding,
.monaco-editor .margin-view-overlays .folding.alwaysShowFoldIcons {
	opacity: 1;
}

.monaco-editor .margin-view-overlays .folding.collapsed {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTUgMTUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDE1IDE1OyI+CjxyZWN0IHg9IjMiIHk9IjMiIHN0eWxlPSJmaWxsOiNFOEU4RTgiIHdpZHRoPSI5IiBoZWlnaHQ9IjkiLz4KPHBhdGggc3R5bGU9ImZpbGw6I0I2QjZCNiIgZD0iTTExLDR2N0g0VjRIMTEgTTEyLDNIM3Y5aDlWM0wxMiwzeiIvPgo8bGluZSBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojNkI2QjZCO3N0cm9rZS1taXRlcmxpbWl0OjEwIiB4MT0iMTAiIHkxPSI3LjUiIHgyPSI1IiB5Mj0iNy41Ii8+CjxsaW5lIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiM2QjZCNkI7c3Ryb2tlLW1pdGVybGltaXQ6MTAiIHgxPSI3LjUiIHkxPSI1IiB4Mj0iNy41IiB5Mj0iMTAiLz4KPC9zdmc+");
	opacity: 1;
}

.monaco-editor.hc-black .margin-view-overlays .folding.collapsed,
.monaco-editor.vs-dark .margin-view-overlays .folding.collapsed {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTUgMTUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDE1IDE1OyI+CjxyZWN0IHg9IjMiIHk9IjMiIHN0eWxlPSJvcGFjaXR5OjAuMTtmaWxsOiNGRkZGRkYiIHdpZHRoPSI5IiBoZWlnaHQ9IjkiLz4KPHBhdGggc3R5bGU9ImZpbGw6IzVBNUE1QSIgZD0iTTExLDR2N0g0VjRIMTEgTTEyLDNIM3Y5aDlWM0wxMiwzeiIvPgo8bGluZSBzdHlsZT0iZmlsbDpub25lO3N0cm9rZTojQzVDNUM1O3N0cm9rZS1taXRlcmxpbWl0OjEwIiB4MT0iMTAiIHkxPSI3LjUiIHgyPSI1IiB5Mj0iNy41Ii8+CjxsaW5lIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlOiNDNUM1QzU7c3Ryb2tlLW1pdGVybGltaXQ6MTAiIHgxPSI3LjUiIHkxPSI1IiB4Mj0iNy41IiB5Mj0iMTAiLz4KPC9zdmc+");
}

.monaco-editor .inline-folded:after {
	color: grey;
	margin: 0.1em 0.2em 0 0.2em;
	content: "⋯";
	display: inline;
	line-height: 1em;
	cursor: pointer;
}

</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -- zone widget */
.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget {
	border-top-width: 1px;
	border-bottom-width: 1px;
}

.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget.results-loaded {
	-webkit-transition: height 100ms ease-in;
	transition: height 100ms ease-in;
}

.monaco-editor .reference-zone-widget .inline {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .reference-zone-widget .messages {
	height: 100%;
	width: 100%;
	text-align: center;
	padding: 3em 0;
}

.monaco-editor .reference-zone-widget .ref-tree {
	line-height: 23px;
}

.monaco-editor .reference-zone-widget .ref-tree .reference {
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file {
	display: inline-flex;
	width: 100%;
	height: 100%;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count {
	margin-right: 12px;
	margin-left: auto;
}

/* High Contrast Theming */

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file {
	font-weight: bold;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 0.2em 0.5em;
	border-radius: 1em;
	font-size: 85%;
	font-weight: normal;
	text-align: center;
	display: inline;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/Microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-description-container {
	overflow: hidden; /* this causes the label/description to shrink first if decorations are enabled */
	text-overflow: ellipsis;
}

.monaco-icon-label > .monaco-icon-label-description-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-description-container > .label-description {
	opacity: 0.7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label.italic > .monaco-icon-label-description-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-label-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	padding: 0 12px 0 5px;
	margin-left: auto;
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-tree.focused .selected .monaco-icon-label, /* tree */
.monaco-tree.focused .selected .monaco-icon-label::after,
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .peekview-widget .head {
	-webkit-box-sizing:	border-box;
	-o-box-sizing: border-box;
	-moz-box-sizing: border-box;
	-ms-box-sizing: border-box;
	box-sizing:	border-box;
	display: flex;
}

.monaco-editor .peekview-widget .head .peekview-title {
	display: inline-block;
	font-size: 13px;
	margin-left: 20px;
	cursor: pointer;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) {
	font-size: 0.9em;
	margin-left: 0.5em;
}

.monaco-editor .peekview-widget .head .peekview-actions {
	flex: 1;
	text-align: right;
	padding-right: 2px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar {
	display: inline-block;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar,
.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar > .actions-container {
	height: 100%;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-item {
	margin-left: 4px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-label {
	width: 16px;
	height: 100%;
	margin: 0;
	line-height: inherit;
	background-repeat: no-repeat;
	background-position: center center;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-label.octicon {
	margin: 0;
}

.monaco-editor .peekview-widget .head .peekview-actions .action-label.icon.close-peekview-action {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iIzQyNDI0MiIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==") center center no-repeat;
}

.monaco-editor .peekview-widget > .body {
	border-top: 1px solid;
	position: relative;
}

/* Dark Theme */
/* High Contrast Theme */

.monaco-editor.hc-black .peekview-widget .head .peekview-actions .action-label.icon.close-peekview-action,
.monaco-editor.vs-dark .peekview-widget .head .peekview-actions .action-label.icon.close-peekview-action {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iI2U4ZThlOCIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==") center center no-repeat;
}

</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .zone-widget {
	position: absolute;
	z-index: 10;
}


.monaco-editor .zone-widget .zone-widget-container {
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-width: 0;
	border-bottom-width: 0;
	position: relative;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .monaco-editor-overlaymessage {
	padding-bottom: 8px;
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeIn {
	animation: fadeIn 150ms ease-out;
}

@keyframes fadeOut {
	from { opacity: 1; }
	to { opacity: 0; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeOut {
	animation: fadeOut 100ms ease-out;
}

.monaco-editor .monaco-editor-overlaymessage .message {
	padding: 1px 4px;
}

.monaco-editor .monaco-editor-overlaymessage .anchor {
	width: 0 !important;
	height: 0 !important;
	border-color: transparent;
	border-style: solid;
	z-index: 1000;
	border-width: 8px;
	position: absolute;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .goto-definition-link {
	text-decoration: underline;
	cursor: pointer;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* marker zone */

.monaco-editor .marker-widget {
	padding-left: 2px;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .marker-widget > .stale {
	opacity: 0.6;
	font-style: italic;
}

.monaco-editor .marker-widget div.block {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .marker-widget .title {
	display: inline-block;
	padding-right: 5px;
}

.monaco-editor .marker-widget .descriptioncontainer {
	position: relative;
	white-space: pre;
	-webkit-user-select: text;
	user-select: text;
}

.monaco-editor .marker-widget .descriptioncontainer .filename {
	cursor: pointer;
	opacity: 0.6;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor-hover {
	cursor: default;
	position: absolute;
	overflow: hidden;
	z-index: 50;
	-webkit-user-select: text;
	-ms-user-select: text;
	-khtml-user-select: text;
	-moz-user-select: text;
	-o-user-select: text;
	user-select: text;
	box-sizing: initial;
	animation: fadein 100ms linear;
	line-height: 1.5em;
}

.monaco-editor-hover.hidden {
	display: none;
}

.monaco-editor-hover .monaco-editor-hover-content {
	max-width: 500px;
}

.monaco-editor-hover .hover-row {
	padding: 4px 5px;
}

.monaco-editor-hover p,
.monaco-editor-hover ul {
	margin: 8px 0;
}

.monaco-editor-hover p:first-child,
.monaco-editor-hover ul:first-child {
	margin-top: 0;
}

.monaco-editor-hover p:last-child,
.monaco-editor-hover ul:last-child {
	margin-bottom: 0;
}

.monaco-editor-hover ul {
	padding-left: 20px;
}

.monaco-editor-hover li > p {
	margin-bottom: 0;
}

.monaco-editor-hover li > ul {
	margin-top: 0;
}

.monaco-editor-hover code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor-hover .monaco-tokenized-source {
	white-space: pre-wrap;
	word-break: break-all;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.colorpicker-widget {
	height: 190px;
	user-select: none;
}

.monaco-editor .colorpicker-hover:focus {
	outline: none;
}


/* Header */

.colorpicker-header {
	display: flex;
	height: 24px;
	position: relative;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-header .picked-color {
	width: 216px;
	text-align: center;
	line-height: 24px;
	cursor: pointer;
	color: white;
	flex: 1;
	text-align: center;
}

.colorpicker-header .picked-color.light {
	color: black;
}

.colorpicker-header .original-color {
	width: 74px;
	z-index: inherit;
	cursor: pointer;
}


/* Body */

.colorpicker-body {
	display: flex;
	padding: 8px;
	position: relative;
}

.colorpicker-body .saturation-wrap {
	overflow: hidden;
	height: 150px;
	position: relative;
	min-width: 220px;
	flex: 1;
}

.colorpicker-body .saturation-box {
	height: 150px;
	position: absolute;
}

.colorpicker-body .saturation-selection {
	width: 9px;
	height: 9px;
	margin: -5px 0 0 -5px;
	border: 1px solid rgb(255, 255, 255);
	border-radius: 100%;
	box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.8);
	position: absolute;
}

.colorpicker-body .strip {
	width: 25px;
	height: 150px;
}

.colorpicker-body .hue-strip {
	position: relative;
	margin-left: 8px;
	cursor: -webkit-grab;
	background: linear-gradient(to bottom, #ff0000 0%, #ffff00 17%, #00ff00 33%, #00ffff 50%, #0000ff 67%, #ff00ff 83%, #ff0000 100%);
}

.colorpicker-body .opacity-strip {
	position: relative;
	margin-left: 8px;
	cursor: -webkit-grab;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-body .strip.grabbing {
	cursor: -webkit-grabbing;
}

.colorpicker-body .slider {
	position: absolute;
	top: 0;
	left: -2px;
	width: calc(100% + 4px);
	height: 4px;
	box-sizing: border-box;
	border: 1px solid rgba(255, 255, 255, 0.71);
	box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.85);
}

.colorpicker-body .strip .overlay {
	height: 150px;
	pointer-events: none;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .detected-link,
.monaco-editor .detected-link-active {
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .detected-link-active {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .parameter-hints-widget {
	z-index: 10;
	display: flex;
	flex-direction: column;
	line-height: 1.5em;
}

.monaco-editor .parameter-hints-widget > .wrapper {
	max-width: 440px;
	display: flex;
	flex-direction: column;
}

.monaco-editor .parameter-hints-widget.multiple {
	min-height: 3.3em;
	padding: 0 0 0 1.9em;
}

.monaco-editor .parameter-hints-widget.visible {
	-webkit-transition: left .05s ease-in-out;
	-moz-transition: left .05s ease-in-out;
	-o-transition: left .05s ease-in-out;
	transition: left .05s ease-in-out;
}

.monaco-editor .parameter-hints-widget p,
.monaco-editor .parameter-hints-widget ul {
	margin: 8px 0;
}

.monaco-editor .parameter-hints-widget .monaco-scrollable-element,
.monaco-editor .parameter-hints-widget .body {
	display: flex;
	flex-direction: column;
}

.monaco-editor .parameter-hints-widget .signature {
	padding: 4px 5px;
}

.monaco-editor .parameter-hints-widget .docs {
	padding: 0 10px 0 5px;
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs.markdown-docs {
	white-space: initial;
}

.monaco-editor .parameter-hints-widget .docs .code {
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .parameter-hints-widget .buttons {
	position: absolute;
	display: none;
	bottom: 0;
	left: 0;
}

.monaco-editor .parameter-hints-widget.multiple .buttons {
	display: block;
}

.monaco-editor .parameter-hints-widget.multiple .button {
	position: absolute;
	left: 2px;
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .button.previous {
	bottom: 24px;
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iIzQyNDI0MiIgZD0iTTEwLjggOS41bC45LS45TDguMSA1IDQuMiA4LjZsLjkuOSAzLTIuNyAyLjcgMi43eiIvPjwvc3ZnPg==");
}

.monaco-editor .parameter-hints-widget .button.next {
	bottom: 0;
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iIzQyNDI0MiIgZD0iTTUuMSA1bC0uOS45IDMuNiAzLjYgMy45LTMuNi0xLS45LTMgMi43TDUuMSA1eiIvPjwvc3ZnPg==");
}

.monaco-editor .parameter-hints-widget .overloads {
	position: absolute;
	display: none;
	text-align: center;
	bottom: 14px;
	left: 0;
	width: 22px;
	height: 12px;
	line-height: 12px;
	opacity: 0.5;
}

.monaco-editor .parameter-hints-widget.multiple .overloads {
	display: block;
}

.monaco-editor .parameter-hints-widget .signature .parameter {
	display: inline-block;
}

.monaco-editor .parameter-hints-widget .signature .parameter.active {
	font-weight: bold;
	text-decoration: underline;
}

.monaco-editor .parameter-hints-widget .documentation-parameter > .parameter {
	font-weight: bold;
	margin-right: 0.5em;
}

/*** VS Dark & High Contrast*/

.monaco-editor.hc-black .parameter-hints-widget .button.previous,
.monaco-editor.vs-dark .parameter-hints-widget .button.previous {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI0U4RThFOCIgZD0iTTEwLjggOS41bC45LS45TDguMSA1IDQuMiA4LjZsLjkuOSAzLTIuNyAyLjcgMi43eiIvPjwvc3ZnPg==");
}

.monaco-editor.hc-black .parameter-hints-widget .button.next,
.monaco-editor.vs-dark .parameter-hints-widget .button.next {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI0U4RThFOCIgZD0iTTUuMSA1bC0uOS45IDMuNiAzLjYgMy45LTMuNi0xLS45LTMgMi43TDUuMSA1eiIvPjwvc3ZnPg==");
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .lightbulb-glyph {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 16px;
	width: 20px;
	padding-left: 2px;
}

.monaco-editor .lightbulb-glyph:hover {
	cursor: pointer;
	/* transform: scale(1.3, 1.3); */
}

.monaco-editor.vs .lightbulb-glyph {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+PHBhdGggZmlsbD0iI0Y2RjZGNiIgZD0iTTEzLjUgNC4yQzEzLjEgMi4xIDEwLjggMCA5LjMgMEg2LjdjLS40IDAtLjYuMi0uNi4yQzQgLjggMi41IDIuNyAyLjUgNC45YzAgLjUtLjEgMi4zIDEuNyAzLjguNS41IDEuMiAyIDEuMyAyLjR2My4zTDcuMSAxNmgybDEuNS0xLjZWMTFjLjEtLjQuOC0xLjkgMS4zLTIuMyAxLjEtLjkgMS41LTEuOSAxLjYtMi43VjQuMnoiLz48Zz48ZyBmaWxsPSIjODQ4NDg0Ij48cGF0aCBkPSJNNi41IDEyaDN2MWgtM3pNNy41IDE1aDEuMWwuOS0xaC0zeiIvPjwvZz48cGF0aCBmaWxsPSIjZmMwIiBkPSJNMTIuNiA1YzAtMi4zLTEuOC00LjEtNC4xLTQuMS0uMSAwLTEuNC4xLTEuNC4xLTIuMS4zLTMuNyAyLTMuNyA0IDAgLjEtLjIgMS42IDEuNCAzIC43LjcgMS41IDIuNCAxLjYgMi45bC4xLjFoM2wuMS0uMmMuMS0uNS45LTIuMiAxLjYtMi45IDEuNi0xLjMgMS40LTIuOCAxLjQtMi45em0tMyAxbC0uNSAzaC0uNlY2YzEuMSAwIC45LTEgLjktMUg2LjV2LjFjMCAuMi4xLjkgMSAuOXYzSDdsLS4yLS43TDYuNSA2Yy0uNyAwLS45LS40LTEtLjd2LS40YzAtLjguOS0uOS45LS45aDMuMXMxIC4xIDEgMWMwIDAgLjEgMS0uOSAxeiIvPjwvZz48cGF0aCBmaWxsPSIjRjBFRkYxIiBkPSJNMTAuNSA1YzAtLjktMS0xLTEtMUg2LjRzLS45LjEtLjkuOXYuNGMwIC4zLjMuNy45LjdsLjQgMi4zLjIuN2guNVY2Yy0xIDAtMS0uNy0xLS45VjVoM3MuMSAxLS45IDF2M2guNmwuNS0zYy45IDAgLjgtMSAuOC0xeiIvPjwvc3ZnPg==") center center no-repeat;
}

.monaco-editor.vs-dark .lightbulb-glyph,
.monaco-editor.hc-black .lightbulb-glyph {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTYgMTYiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+PHBhdGggZmlsbD0iIzFFMUUxRSIgZD0iTTEzLjUgNC4yQzEzLjEgMi4xIDEwLjggMCA5LjMgMEg2LjdjLS40IDAtLjYuMi0uNi4yQzQgLjggMi41IDIuNyAyLjUgNC45YzAgLjUtLjEgMi4zIDEuNyAzLjguNS41IDEuMiAyIDEuMyAyLjR2My4zTDcuMSAxNmgybDEuNS0xLjZWMTFjLjEtLjQuOC0xLjkgMS4zLTIuMyAxLjEtLjkgMS41LTEuOSAxLjYtMi43VjQuMnoiLz48Zz48ZyBmaWxsPSIjQzVDNUM1Ij48cGF0aCBkPSJNNi41IDEyaDN2MWgtM3pNNy41IDE1aDEuMWwuOS0xaC0zeiIvPjwvZz48cGF0aCBmaWxsPSIjRERCMjA0IiBkPSJNMTIuNiA1YzAtMi4zLTEuOC00LjEtNC4xLTQuMS0uMSAwLTEuNC4xLTEuNC4xLTIuMS4zLTMuNyAyLTMuNyA0IDAgLjEtLjIgMS42IDEuNCAzIC43LjcgMS41IDIuNCAxLjYgMi45bC4xLjFoM2wuMS0uMmMuMS0uNS45LTIuMiAxLjYtMi45IDEuNi0xLjMgMS40LTIuOCAxLjQtMi45em0tMyAxbC0uNSAzaC0uNlY2YzEuMSAwIC45LTEgLjktMUg2LjV2LjFjMCAuMi4xLjkgMSAuOXYzSDdsLS4yLS43TDYuNSA2Yy0uNyAwLS45LS40LTEtLjd2LS40YzAtLjguOS0uOS45LS45aDMuMXMxIC4xIDEgMWMwIDAgLjEgMS0uOSAxeiIvPjwvZz48cGF0aCBmaWxsPSIjMjUyNTI2IiBkPSJNMTAuNSA1YzAtLjktMS0xLTEtMUg2LjRzLS45LjEtLjkuOXYuNGMwIC4zLjMuNy45LjdsLjQgMi4zLjIuN2guNVY2Yy0xIDAtMS0uNy0xLS45VjVoM3MuMSAxLS45IDF2M2guNmwuNS0zYy45IDAgLjgtMSAuOC0xeiIvPjwvc3ZnPg==") center center no-repeat;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .rename-box {
	z-index: 100;
	color: inherit;
}

.monaco-editor .rename-box .rename-input {
	padding: 4px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs		.snippet-placeholder { background-color: rgba(10, 50, 100, 0.2); min-width: 2px; }
.monaco-editor.vs-dark	.snippet-placeholder { background-color: rgba(124, 124, 124, 0.3); min-width: 2px; }
.monaco-editor.hc-black	.snippet-placeholder { background-color: rgba(124, 124, 124, 0.3); min-width: 2px; }

.monaco-editor.vs		.finish-snippet-placeholder { outline: rgba(10, 50, 100, 0.5) solid 1px; }
.monaco-editor.vs-dark	.finish-snippet-placeholder	{ outline: #525252 solid 1px; }
.monaco-editor.hc-black	.finish-snippet-placeholder	{ outline: #525252 solid 1px; }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Suggest widget*/
.monaco-editor .suggest-widget {
	z-index: 40;
}

/** Initial widths **/

.monaco-editor .suggest-widget {
	width: 430px;
}

.monaco-editor .suggest-widget > .message,
.monaco-editor .suggest-widget > .tree,
.monaco-editor .suggest-widget > .details {
	width: 100%;
	border-style: solid;
	border-width: 1px;
	box-sizing: border-box;
}

.monaco-editor.hc-black .suggest-widget > .message,
.monaco-editor.hc-black .suggest-widget > .tree,
.monaco-editor.hc-black .suggest-widget > .details {
	border-width: 2px;
}

/** Adjust width when docs are expanded to the side **/
.monaco-editor .suggest-widget.docs-side {
	width: 660px;
}

.monaco-editor .suggest-widget.docs-side > .tree,
.monaco-editor .suggest-widget.docs-side > .details {
	width: 50%;
	float: left;
}

.monaco-editor .suggest-widget.docs-side.list-right > .tree,
.monaco-editor .suggest-widget.docs-side.list-right > .details  {
	float: right;
}


/* Styles for Message element for when widget is loading or is empty */
.monaco-editor .suggest-widget > .message {
	padding-left: 22px;
}

/** Styles for the list element **/
.monaco-editor .suggest-widget > .tree {
	height: 100%;
}



/** Styles for each row in the list element **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding-right: 10px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents {
	flex: 1;
	height: 100%;
	overflow: hidden;
	padding-left: 2px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main {
	display: flex;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: pre;
}

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .highlight {
	font-weight: bold;
}

/** Icon styles **/

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .close,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .readMore {
	opacity: 0.6;
	background-position: center center;
	background-repeat: no-repeat;
	background-size: 70%;
	cursor: pointer;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .close {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iIzQyNDI0MiIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==");
	float: right;
	margin-right: 5px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .readMore {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTggMWMtMy44NjUgMC03IDMuMTM1LTcgN3MzLjEzNSA3IDcgNyA3LTMuMTM1IDctNy0zLjEzNS03LTctN3ptMSAxMmgtMnYtN2gydjd6bTAtOGgtMnYtMmgydjJ6IiBmaWxsPSIjMUJBMUUyIi8+PHBhdGggZD0iTTcgNmgydjdoLTJ2LTd6bTAtMWgydi0yaC0ydjJ6IiBmaWxsPSIjZmZmIi8+PC9zdmc+");
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .close:hover,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .readMore:hover {
	opacity: 1;
}

/** Type Info and icon next to the label in the focused completion item **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .type-label {
	margin-left: 0.8em;
	flex: 1;
	text-align: right;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .type-label > .monaco-tokenized-source {
	display: inline;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .readMore,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .type-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused > .contents > .main > .readMore,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused > .contents > .main > .type-label,
.monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row.focused > .contents > .main > .readMore {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused > .contents > .main > .readMore,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused > .contents > .main > .type-label {
	display: inline;
}

/** Styles for each row in the list **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon {
	display: block;
	height: 16px;
	width: 16px;
	background-repeat: no-repeat;
	background-size: 80%;
	background-position: center;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDEwYzAgMi4yMDUtMS43OTQgNC00IDQtMS44NTggMC0zLjQxMS0xLjI3OS0zLjg1OC0zaC0uOTc4bDIuMzE4IDRIMHYtMS43MDNsMi0zLjQwOFYwaDExdjYuMTQyYzEuNzIxLjQ0NyAzIDIgMyAzLjg1OHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0xMiAxdjQuNzVBNC4yNTUgNC4yNTUgMCAwIDAgNy43NSAxMGgtLjczMkw0LjI3NSA1LjI2OSAzIDcuNDQyVjFoOXpNNy43NDcgMTRMNC4yNjkgOCAuNzQ4IDE0aDYuOTk5ek0xNSAxMGEzIDMgMCAxIDEtNiAwIDMgMyAwIDAgMSA2IDB6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.method,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.function,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.constructor { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1wdXJwbGV7ZmlsbDojNjUyZDkwfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE1IDMuMzQ5djguNDAzTDguOTc1IDE2SDguMDdMMSAxMS41ODJWMy4zMjdMNy41OTUgMGgxLjExOEwxNSAzLjM0OXoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0xMi43MTUgNC4zOThMOC40ODcgNy4wMiAzLjU2NSA0LjI3Mmw0LjU3OC0yLjMwOSA0LjU3MiAyLjQzNXpNMyA1LjEwMmw1IDIuNzkydjUuNzA1bC01LTMuMTI1VjUuMTAyem02IDguNDM0VjcuODc4bDQtMi40OHY1LjMxN2wtNCAyLjgyMXoiIGlkPSJpY29uRmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tcHVycGxlIiBkPSJNOC4xNTYuODM3TDIgMy45NDJ2Ny4wODVMOC41MTcgMTUuMSAxNCAxMS4yMzNWMy45NUw4LjE1Ni44Mzd6bTQuNTU5IDMuNTYxTDguNDg3IDcuMDIgMy41NjUgNC4yNzJsNC41NzgtMi4zMDkgNC41NzIgMi40MzV6TTMgNS4xMDJsNSAyLjc5MnY1LjcwNWwtNS0zLjEyNVY1LjEwMnptNiA4LjQzNFY3Ljg3OGw0LTIuNDh2NS4zMTdsLTQgMi44MjF6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.field { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6IzAwNTM5Y308L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0wIDEwLjczNlY0LjVMOSAwbDcgMy41djYuMjM2bC05IDQuNS03LTMuNXoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik05IDFMMSA1djVsNiAzIDgtNFY0TDkgMXpNNyA2Ljg4MkwzLjIzNiA1IDkgMi4xMTggMTIuNzY0IDQgNyA2Ljg4MnoiIGlkPSJpY29uQmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTkgMi4xMThMMTIuNzY0IDQgNyA2Ljg4MiAzLjIzNiA1IDkgMi4xMTh6IiBpZD0iaWNvbkZnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.event { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYWN0aW9uLW9yYW5nZXtmaWxsOiNjMjdkMWF9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTQgMS40MTRMOS40MTQgNkgxNHYxLjQxNEw1LjQxNCAxNkgzdi0xLjIzNEw1LjM3MSAxMEgyVjguNzY0TDYuMzgyIDBIMTR2MS40MTR6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLW9yYW5nZSIgZD0iTTcgN2g2bC04IDhINGwyLjk4NS02SDNsNC04aDZMNyA3eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.operator { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6IzAwNTM5Y308L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xIDF2MTRoMTRWMUgxem02IDEySDN2LTFoNHYxem0wLTNIM1Y5aDR2MXptMC01SDV2Mkg0VjVIMlY0aDJWMmgxdjJoMnYxem0zLjI4MSA4SDguNzE5bDMtNGgxLjU2M2wtMy4wMDEgNHpNMTQgNUg5VjRoNXYxeiIgaWQ9Imljb25CZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNNyA1SDV2Mkg0VjVIMlY0aDJWMmgxdjJoMnYxem03LTFIOXYxaDVWNHpNNyA5SDN2MWg0Vjl6bTAgM0gzdjFoNHYtMXptMy4yODEgMWwzLTRoLTEuNTYzbC0zIDRoMS41NjN6IiBpZD0iaWNvbkZnIiBzdHlsZT0iZGlzcGxheTogbm9uZTsiLz48L3N2Zz4="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.variable { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiMwMDUzOWN9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTEgM3YxLjAxNUw4LjczMyAyLjg4MiA1IDQuNzQ5VjNIMHYxMGg1di0xLjg1OWwyLjE1NiAxLjA3N0wxMSAxMC4yOTVWMTNoNVYzaC01eiIgaWQ9Im91dGxpbmUiIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMiA1djZoMnYxSDFWNGgzdjFIMnptMTAgNnYxaDNWNGgtM3YxaDJ2NmgtMnoiIGlkPSJpY29uQmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTcuMTU2IDcuMTU2bC0xLjU3OC0uNzg5IDMuMTU2LTEuNTc4IDEuNTc4Ljc4OS0zLjE1NiAxLjU3OHoiIGlkPSJpY29uRmciIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWFjdGlvbi1ibHVlIiBkPSJNOC43MzMgNEw0IDYuMzY3djMuMTU2TDcuMTU2IDExLjFsNC43MzMtMi4zNjdWNS41NzhMOC43MzMgNHpNNy4xNTYgNy4xNTZsLTEuNTc4LS43ODkgMy4xNTYtMS41NzggMS41NzguNzg5LTMuMTU2IDEuNTc4eiIgaWQ9ImNvbG9ySW1wb3J0YW5jZSIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.class { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYWN0aW9uLW9yYW5nZXtmaWxsOiNjMjdkMWF9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTYgNi41ODZsLTMtM0wxMS41ODYgNUg5LjQxNGwxLTEtNC00aC0uODI4TDAgNS41ODZ2LjgyOGw0IDRMNi40MTQgOEg3djVoMS41ODZsMyAzaC44MjhMMTYgMTIuNDE0di0uODI4TDEzLjkxNCA5LjUgMTYgNy40MTR2LS44Mjh6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWFjdGlvbi1vcmFuZ2UiIGQ9Ik0xMyAxMGwyIDItMyAzLTItMiAxLTFIOFY3SDZMNCA5IDEgNmw1LTUgMyAzLTIgMmg1bDEtMSAyIDItMyAzLTItMiAxLTFIOXY0bDIuOTk5LjAwMkwxMyAxMHoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.interface { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6IzAwNTM5Y308L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xMS41IDEyYy0xLjkxNSAwLTMuNjAyLTEuMjQxLTQuMjI4LTNoLTEuNDFhMy4xMSAzLjExIDAgMCAxLTIuNzM3IDEuNjI1QzEuNDAyIDEwLjYyNSAwIDkuMjIzIDAgNy41czEuNDAyLTMuMTI1IDMuMTI1LTMuMTI1YzEuMTY1IDAgMi4yMDEuNjM5IDIuNzM3IDEuNjI1aDEuNDFjLjYyNi0xLjc1OSAyLjMxMy0zIDQuMjI4LTNDMTMuOTgxIDMgMTYgNS4wMTkgMTYgNy41UzEzLjk4MSAxMiAxMS41IDEyeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTExLjUgOUExLjUwMSAxLjUwMSAwIDEgMSAxMyA3LjVjMCAuODI2LS42NzMgMS41LTEuNSAxLjV6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMS41IDRhMy40OSAzLjQ5IDAgMCAwLTMuNDUgM0g1LjE4NUEyLjEyMiAyLjEyMiAwIDAgMCAxIDcuNWEyLjEyMyAyLjEyMyAwIDEgMCA0LjE4NS41SDguMDVhMy40OSAzLjQ5IDAgMCAwIDMuNDUgMyAzLjUgMy41IDAgMSAwIDAtN3ptMCA1Yy0uODI3IDAtMS41LS42NzMtMS41LTEuNVMxMC42NzMgNiAxMS41IDZzMS41LjY3MyAxLjUgMS41UzEyLjMyNyA5IDExLjUgOXoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.struct { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYWN0aW9uLWJsdWV7ZmlsbDojMDA1MzljfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTkgMTRWOEg3djZIMVYyaDE0djEySDl6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMCA5aDR2NGgtNFY5em0tOCA0aDRWOUgydjR6TTIgM3Y0aDEyVjNIMnoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.type-parameter { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTEwLjcwMiAxMC41bDItMi0yLTIgLjUtLjVIMTB2NWgxdjNINXYtM2gxVjZINC43OThsLjUuNS0yIDIgMiAyTDMgMTIuNzk3bC0zLTNWNy4yMDFsMy0zVjJoMTB2Mi4yMDFsMyAzdjIuNTk2bC0zIDMtMi4yOTgtMi4yOTd6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik00IDNoOHYyaC0xdi0uNWMwLS4yNzctLjIyNC0uNS0uNS0uNUg5djcuNWMwIC4yNzUuMjI0LjUuNS41aC41djFINnYtMWguNWEuNS41IDAgMCAwIC41LS41VjRINS41YS41LjUgMCAwIDAtLjUuNVY1SDRWM3pNMyA1LjYxNUwuMTE2IDguNSAzIDExLjM4M2wuODg0LS44ODMtMi0yIDItMkwzIDUuNjE1em0xMCAwbC0uODg0Ljg4NSAyIDItMiAyIC44ODQuODgzTDE1Ljg4NCA4LjUgMTMgNS42MTV6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.module { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTkuMjYgMTEuOTg0bC45NzgtLjAyMWEuOTYyLjk2MiAwIDAgMCAuMDktLjAwNmMuMDExLS4wNjMuMDI2LS4xNzkuMDI2LS4zNjFWOS42ODhjMC0uNjc5LjE4NS0xLjI1Ny41My0xLjcwNy0uMzQ2LS40NTItLjUzLTEuMDMtLjUzLTEuNzA1VjQuMzVjMC0uMTY3LS4wMjEtLjI1OS0uMDM0LS4zMDJMOS4yNiA0LjAyVi45NzNsMS4wMTEuMDExYzIuMTY3LjAyNCAzLjQwOSAxLjE1NiAzLjQwOSAzLjEwNXYxLjk2MmMwIC4zNTEuMDcxLjQ2MS4wNzIuNDYybC45MzYuMDYuMDUzLjkyN3YxLjkzNmwtLjkzNi4wNjFjLS4wNzYuMDE2LS4xMjUuMTQ2LS4xMjUuNDI0djIuMDE3YzAgLjkxNC0uMzMyIDMuMDQzLTMuNDA4IDMuMDc4bC0xLjAxMi4wMTF2LTMuMDQzem0tMy41MjEgMy4wMzJjLTMuMDg5LS4wMzUtMy40MjItMi4xNjQtMy40MjItMy4wNzhWOS45MjFjMC0uMzI3LS4wNjYtLjQzMi0uMDY3LS40MzNsLS45MzctLjA2LS4wNjMtLjkyOVY2LjU2M2wuOTQyLS4wNmMuMDU4IDAgLjEyNS0uMTE0LjEyNS0uNDUyVjQuMDljMC0xLjk0OSAxLjI0OC0zLjA4MSAzLjQyMi0zLjEwNUw2Ljc1Ljk3M1Y0LjAybC0uOTc1LjAyM2EuNTcyLjU3MiAwIDAgMC0uMDkzLjAxYy4wMDYuMDIxLS4wMTkuMTE1LS4wMTkuMjk3djEuOTI4YzAgLjY3NS0uMTg2IDEuMjUzLS41MzQgMS43MDUuMzQ4LjQ1LjUzNCAxLjAyOC41MzQgMS43MDd2MS45MDdjMCAuMTc1LjAxNC4yOTEuMDI3LjM2My4wMjMuMDAyIDEuMDYuMDI1IDEuMDYuMDI1djMuMDQzbC0xLjAxMS0uMDEyeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTUuNzUgMTQuMDE2Yy0xLjYyMy0uMDE5LTIuNDM0LS43MTEtMi40MzQtMi4wNzhWOS45MjFjMC0uOTAyLS4zNTUtMS4zNzYtMS4wNjYtMS40MjJ2LS45OThjLjcxMS0uMDQ1IDEuMDY2LS41MjkgMS4wNjYtMS40NDlWNC4wOWMwLTEuMzg1LjgxMS0yLjA4NyAyLjQzNC0yLjEwNXYxLjA2Yy0uNzI1LjAxNy0xLjA4Ny40NTMtMS4wODcgMS4zMDV2MS45MjhjMCAuOTItLjQ1NCAxLjQ4OC0xLjM2IDEuNzAyVjhjLjkwNy4yMDEgMS4zNi43NjMgMS4zNiAxLjY4OHYxLjkwN2MwIC40ODguMDgxLjgzNS4yNDMgMS4wNDIuMTYyLjIwOC40NDMuMzE2Ljg0NC4zMjV2MS4wNTR6bTcuOTktNS41MTdjLS43MDYuMDQ1LTEuMDYuNTItMS4wNiAxLjQyMnYyLjAxN2MwIDEuMzY3LS44MDcgMi4wNi0yLjQyIDIuMDc4di0xLjA1M2MuMzk2LS4wMDkuNjc4LS4xMTguODQ0LS4zMjguMTY3LS4yMS4yNS0uNTU2LjI1LTEuMDM5VjkuNjg4YzAtLjkyNS40NDktMS40ODggMS4zNDctMS42ODh2LS4wMjFjLS44OTgtLjIxNC0xLjM0Ny0uNzgyLTEuMzQ3LTEuNzAyVjQuMzVjMC0uODUyLS4zNjQtMS4yODgtMS4wOTQtMS4zMDZ2LTEuMDZjMS42MTMuMDE4IDIuNDIuNzIgMi40MiAyLjEwNXYxLjk2MmMwIC45Mi4zNTQgMS40MDQgMS4wNiAxLjQ0OXYuOTk5eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.property { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDUuNWE1LjUgNS41IDAgMCAxLTUuNSA1LjVjLS4yNzUgMC0uNTQzLS4wMjctLjgwNy0uMDY2bC0uMDc5LS4wMTJhNS40MjkgNS40MjkgMCAwIDEtLjgxLS4xOTJsLTQuNTM3IDQuNTM3Yy0uNDcyLjQ3My0xLjEuNzMzLTEuNzY3LjczM3MtMS4yOTUtLjI2LTEuNzY4LS43MzJhMi41MDIgMi41MDIgMCAwIDEgMC0zLjUzNWw0LjUzNy00LjUzN2E1LjQ1MiA1LjQ1MiAwIDAgMS0uMTkxLS44MTJjLS4wMDUtLjAyNS0uMDA4LS4wNTEtLjAxMi0uMDc3QTUuNTAzIDUuNTAzIDAgMCAxIDUgNS41YTUuNSA1LjUgMCAxIDEgMTEgMHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0xNSA1LjVhNC41IDQuNSAwIDAgMS00LjUgNC41Yy0uNjkzIDAtMS4zNDItLjE3LTEuOTI5LS40NWwtNS4wMSA1LjAxYy0uMjkzLjI5NC0uNjc3LjQ0LTEuMDYxLjQ0cy0uNzY4LS4xNDYtMS4wNjEtLjQzOWExLjUgMS41IDAgMCAxIDAtMi4xMjFsNS4wMS01LjAxQTQuNDgzIDQuNDgzIDAgMCAxIDYgNS41IDQuNSA0LjUgMCAwIDEgMTAuNSAxYy42OTMgMCAxLjM0Mi4xNyAxLjkyOS40NUw5LjYzNiA0LjI0M2wyLjEyMSAyLjEyMSAyLjc5My0yLjc5M2MuMjguNTg3LjQ1IDEuMjM2LjQ1IDEuOTI5eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.unit { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxMS4wMTNIMVY0aDE1djcuMDEzeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTggOUg3VjZoM3YzSDlWN0g4djJ6TTQgN2gxdjJoMVY2SDN2M2gxVjd6bTggMGgxdjJoMVY2aC0zdjNoMVY3eiIgaWQ9Imljb25GZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMiA1djVoMTNWNUgyem00IDRINVY3SDR2MkgzVjZoM3Yzem00IDBIOVY3SDh2Mkg3VjZoM3Yzem00IDBoLTFWN2gtMXYyaC0xVjZoM3YzeiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.constant { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiMwMDUzOWN9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMi44NzkgMTRMMSAxMi4xMjFWMy44NzlMMi44NzkgMmgxMC4yNDJMMTUgMy44Nzl2OC4yNDJMMTMuMTIxIDE0SDIuODc5eiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTEyLjI5MyA0SDMuNzA3TDMgNC43MDd2Ni41ODZsLjcwNy43MDdoOC41ODZsLjcwNy0uNzA3VjQuNzA3TDEyLjI5MyA0ek0xMSAxMEg1VjloNnYxem0wLTNINVY2aDZ2MXoiIGlkPSJpY29uRmciLz48ZyBpZD0iaWNvbkJnIj48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTEyLjcwNyAxM0gzLjI5M0wyIDExLjcwN1Y0LjI5M0wzLjI5MyAzaDkuNDE0TDE0IDQuMjkzdjcuNDE0TDEyLjcwNyAxM3ptLTktMWg4LjU4NmwuNzA3LS43MDdWNC43MDdMMTIuMjkzIDRIMy43MDdMMyA0LjcwN3Y2LjU4NmwuNzA3LjcwN3oiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tYmx1ZSIgZD0iTTExIDdINVY2aDZ2MXptMCAySDV2MWg2Vjl6Ii8+PC9nPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.value,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.enum { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1vcmFuZ2V7ZmlsbDojYzI3ZDFhfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE0LjQxNCAxTDE2IDIuNTg2djUuODI4TDE0LjQxNCAxMEgxMHYzLjQxNkw4LjQxNCAxNUgxLjU4NkwwIDEzLjQxNnYtNS44M0wxLjU4NiA2SDZWMi41ODZMNy41ODYgMWg2LjgyOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0yIDEzaDZWOEgydjV6bTEtNGg0djFIM1Y5em0wIDJoNHYxSDN2LTF6bTExLTVWM0g4djNoLjQxNEw5IDYuNTg2VjZoNHYxSDkuNDE0bC41ODYuNTg2VjhoNFY2em0tMS0xSDlWNGg0djF6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLW9yYW5nZSIgZD0iTTMgMTFoNC4wMDF2MUgzdi0xem0wLTFoNC4wMDFWOUgzdjF6bTYtMnY1bC0xIDFIMmwtMS0xVjhsMS0xaDZsMSAxek04IDhIMnY1aDZWOHptMS0ybDEgMWgzVjZIOXptMC0xaDRWNEg5djF6bTUtM0g4TDcgM3YzaDFWM2g2djVoLTR2MWg0bDEtMVYzbC0xLTF6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.enum-member { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtZmd7ZmlsbDojZjBlZmYxfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6IzAwNTM5Y308L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0wIDE1VjZoNlYyLjU4Nkw3LjU4NSAxaDYuODI5TDE2IDIuNTg2djUuODI5TDE0LjQxNCAxMEgxMHY1SDB6bTMtNnoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik04IDN2M2g1djFoLTN2MWg0VjNIOHptNSAySDlWNGg0djF6TTIgOHY1aDZWOEgyem01IDNIM3YtMWg0djF6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMCA2aDN2MWgtM1Y2ek05IDR2MWg0VjRIOXptNS0ySDhMNyAzdjNoMVYzaDZ2NWgtNHYxaDRsMS0xVjNsLTEtMXptLTcgOEgzdjFoNHYtMXptMi0zdjdIMVY3aDh6TTggOEgydjVoNlY4eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.keyword { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiA1VjJIOVYxSDB2MTRoMTN2LTNoM1Y5aC0xVjZIOVY1aDd6bS04IDdWOWgxdjNIOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0yIDNoNXYxSDJWM3oiIGlkPSJpY29uRmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTE1IDRoLTVWM2g1djF6bS0xIDNoLTJ2MWgyVjd6bS00IDBIMXYxaDlWN3ptMiA2SDF2MWgxMXYtMXptLTUtM0gxdjFoNnYtMXptOCAwaC01djFoNXYtMXpNOCAydjNIMVYyaDd6TTcgM0gydjFoNVYzeiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.text { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxNUgwVjFoMTZ2MTR6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNOS4yMjkgNy4zNTRjLjAzNS4xNDYuMDUyLjMxLjA1Mi40OTQgMCAuMjM0LS4wMi40NDEtLjA2LjYyMS0uMDM5LjE4LS4wOTUuMzI4LS4xNjguNDQ1YS42ODcuNjg3IDAgMCAxLS45MTQuMjgxLjc2Ljc2IDAgMCAxLS4yMzctLjIwNy45ODguOTg4IDAgMCAxLS4xNTQtLjMwNiAxLjI2MiAxLjI2MiAwIDAgMS0uMDU3LS4zODF2LS41MDZjMC0uMTcuMDItLjMyNi4wNjEtLjQ2NXMuMDk2LS4yNTguMTY4LS4zNTlhLjc1Ni43NTYgMCAwIDEgLjI1Ny0uMjMyYy4xLS4wNTUuMjEtLjA4Mi4zMzEtLjA4MmEuNjQ2LjY0NiAwIDAgMSAuNTcxLjMyYy4wNjcuMTA1LjExNi4yMy4xNS4zNzd6bS01LjEyNi44NjlhLjU1Ny41NTcgMCAwIDAtLjE5Ni4xMzJjLS4wNDcuMDUzLS4wOC4xMTItLjA5Ny4xOHMtLjAyOC4xNDctLjAyOC4yMzNhLjUxMy41MTMgMCAwIDAgLjE1Ny4zOS41MjguNTI4IDAgMCAwIC4xODYuMTEzLjY4Mi42ODIgMCAwIDAgLjI0Mi4wNDEuNzYuNzYgMCAwIDAgLjU5My0uMjcxLjg5Ny44OTcgMCAwIDAgLjE2NS0uMjk1Yy4wMzgtLjExMy4wNTktLjIzNC4wNTktLjM2NXYtLjM0NmwtLjc2MS4xMWExLjI5IDEuMjkgMCAwIDAtLjMyLjA3OHpNMTQgM3YxMEgyVjNoMTJ6TTUuOTYyIDcuNDY5YzAtLjIzOC0uMDI3LS40NTEtLjA4My0uNjM3YTEuMjg2IDEuMjg2IDAgMCAwLS4yNDktLjQ3MSAxLjA4IDEuMDggMCAwIDAtLjQyNC0uMjk1IDEuNjQ0IDEuNjQ0IDAgMCAwLS42MDgtLjEwMWMtLjExOSAwLS4yNDEuMDEyLS4zNjguMDMzYTMuMjEzIDMuMjEzIDAgMCAwLS42NzMuMTk1IDEuMzEzIDEuMzEzIDAgMCAwLS4yMTIuMTE0di43NjhjLjE1OC0uMTMyLjM0MS0uMjM1LjU0NC0uMzEzLjIwNC0uMDc4LjQxMy0uMTE3LjYyNy0uMTE3LjIxMyAwIC4zNzcuMDYzLjQ5NC4xODYuMTE2LjEyNS4xNzQuMzI0LjE3NC42bC0xLjAzLjE1NGMtLjIwNS4wMjYtLjM4LjA3Ny0uNTI2LjE1MWExLjA4MyAxLjA4MyAwIDAgMC0uNTYzLjY2QTEuNTYyIDEuNTYyIDAgMCAwIDMgOC44NTdjMCAuMTcuMDI1LjMyMy4wNzQuNDYzYS45NDUuOTQ1IDAgMCAwIC41NjguNTk2Yy4xMzkuMDU3LjI5Ny4wODQuNDc4LjA4NC4yMjkgMCAuNDMxLS4wNTMuNjA0LS4xNmExLjMgMS4zIDAgMCAwIC40MzktLjQ2M2guMDE0di41MjloLjc4NVY3LjQ2OXpNMTAgNy44NjFhMy41NCAzLjU0IDAgMCAwLS4wNzQtLjczNCAyLjA0NyAyLjA0NyAwIDAgMC0uMjI4LS42MTEgMS4yMDMgMS4yMDMgMCAwIDAtLjM5NC0uNDE2IDEuMDMgMS4wMyAwIDAgMC0uNTc0LS4xNTNjLS4xMjMgMC0uMjM0LjAxOC0uMzM2LjA1MWExIDEgMCAwIDAtLjI3OC4xNDcgMS4xNTMgMS4xNTMgMCAwIDAtLjIyNS4yMjIgMi4wMjIgMi4wMjIgMCAwIDAtLjE4MS4yODloLS4wMTNWNUg3djQuODg3aC42OTd2LS40ODVoLjAxM2MuMDQ0LjA4Mi4wOTUuMTU4LjE1MS4yMjkuMDU3LjA3LjExOS4xMzMuMTkxLjE4NmEuODM1LjgzNSAwIDAgMCAuMjM4LjEyMS45NDMuOTQzIDAgMCAwIC4yOTMuMDQyYy4yMyAwIC40MzQtLjA1My42MDktLjE2YTEuMzQgMS4zNCAwIDAgMCAuNDQzLS40NDNjLjEyLS4xODguMjExLS40MTIuMjcyLS42NzJBMy42MiAzLjYyIDAgMCAwIDEwIDcuODYxem0zLTEuNjU4YS43LjcgMCAwIDAtLjEwNi0uMDY2IDEuMTgzIDEuMTgzIDAgMCAwLS4xNDItLjA2MyAxLjIzMyAxLjIzMyAwIDAgMC0uMzYzLS4wNjVjLS4yMDkgMC0uMzk5LjA1MS0uNTY5LjE1YTEuMzU1IDEuMzU1IDAgMCAwLS40MzMuNDI0Yy0uMTE4LjE4Mi0uMjEuNDAyLS4yNzMuNjZhMy42MyAzLjYzIDAgMCAwLS4wMDggMS42MTVjLjA2LjIzLjE0My40My4yNTIuNjAyLjEwOS4xNjguMjQxLjMwMy4zOTYuMzk2YS45NzIuOTcyIDAgMCAwIC41MjQuMTQ0Yy4xNTggMCAuMjk2LS4wMjEuNDEzLS4wNjguMTE3LS4wNDUuMjE5LS4xMDguMzA5LS4xODR2LS43N2ExLjA5NCAxLjA5NCAwIDAgMS0uMjg4LjIyNS44MTkuODE5IDAgMCAxLS4xNTguMDY4LjQ4LjQ4IDAgMCAxLS4xNTMuMDI3LjYyLjYyIDAgMCAxLS4yNzQtLjA3NGMtLjI0MS0uMTM2LS40MjMtLjQ3OS0uNDIzLTEuMTQ2IDAtLjcxNS4yMDYtMS4xMi40NjktMS4zMDEuMDc3LS4wMzIuMTUzLS4wNjQuMjM4LS4wNjQuMTEzIDAgLjIyLjAyNy4zMTcuMDgyLjA5Ni4wNTcuMTg4LjEzMS4yNzIuMjIzdi0uODE1eiIgaWQ9Imljb25GZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMSAydjEyaDE0VjJIMXptMTMgMTFIMlYzaDEydjEwek01LjYzIDYuMzYxYTEuMDggMS4wOCAwIDAgMC0uNDI0LS4yOTUgMS42NDQgMS42NDQgMCAwIDAtLjYwOC0uMTAxYy0uMTE5IDAtLjI0MS4wMTItLjM2OC4wMzNhMy4yMTMgMy4yMTMgMCAwIDAtLjY3My4xOTUgMS4zMTMgMS4zMTMgMCAwIDAtLjIxMi4xMTR2Ljc2OGMuMTU4LS4xMzIuMzQxLS4yMzUuNTQ0LS4zMTMuMjA0LS4wNzguNDEzLS4xMTcuNjI3LS4xMTcuMjEzIDAgLjM3Ny4wNjMuNDk0LjE4Ni4xMTYuMTI1LjE3NC4zMjQuMTc0LjZsLTEuMDMuMTU0Yy0uMjA1LjAyNi0uMzguMDc3LS41MjYuMTUxYTEuMDgzIDEuMDgzIDAgMCAwLS41NjMuNjZBMS41NjIgMS41NjIgMCAwIDAgMyA4Ljg1N2MwIC4xNy4wMjUuMzIzLjA3NC40NjNhLjk0NS45NDUgMCAwIDAgLjU2OC41OTZjLjEzOS4wNTcuMjk3LjA4NC40NzguMDg0LjIyOSAwIC40MzEtLjA1My42MDQtLjE2YTEuMyAxLjMgMCAwIDAgLjQzOS0uNDYzaC4wMTR2LjUyOWguNzg1VjcuNDY5YzAtLjIzOC0uMDI3LS40NTEtLjA4My0uNjM3YTEuMjg2IDEuMjg2IDAgMCAwLS4yNDktLjQ3MXptLS40NDYgMi4wMmMwIC4xMzEtLjAyLjI1Mi0uMDU5LjM2NWEuODk3Ljg5NyAwIDAgMS0uMTY1LjI5NS43NTguNzU4IDAgMCAxLS41OTMuMjcyLjY4Mi42ODIgMCAwIDEtLjI0Mi0uMDQxLjUwNy41MDcgMCAwIDEtLjMwMi0uMjg2LjU4My41ODMgMCAwIDEtLjA0MS0uMjE4YzAtLjA4Ni4wMS0uMTY0LjAyNy0uMjMycy4wNTEtLjEyNy4wOTgtLjE4YS41NDYuNTQ2IDAgMCAxIC4xOTYtLjEzM2MuMDgzLS4wMzMuMTg5LS4wNjEuMzItLjA3OGwuNzYxLS4xMDl2LjM0NXptNC41MTQtMS44NjVhMS4yMDMgMS4yMDMgMCAwIDAtLjM5NC0uNDE2IDEuMDMgMS4wMyAwIDAgMC0uNTc0LS4xNTNjLS4xMjMgMC0uMjM0LjAxOC0uMzM2LjA1MWExIDEgMCAwIDAtLjI3OC4xNDcgMS4xNTMgMS4xNTMgMCAwIDAtLjIyNS4yMjIgMi4wMjIgMi4wMjIgMCAwIDAtLjE4MS4yODloLS4wMTNWNUg3djQuODg3aC42OTd2LS40ODVoLjAxM2MuMDQ0LjA4Mi4wOTUuMTU4LjE1MS4yMjkuMDU3LjA3LjExOS4xMzMuMTkxLjE4NmEuODM1LjgzNSAwIDAgMCAuMjM4LjEyMS45NDMuOTQzIDAgMCAwIC4yOTMuMDQyYy4yMyAwIC40MzQtLjA1My42MDktLjE2YTEuMzQgMS4zNCAwIDAgMCAuNDQzLS40NDNjLjEyLS4xODguMjExLS40MTIuMjcyLS42NzJBMy42MiAzLjYyIDAgMCAwIDEwIDcuODYxYTMuNTQgMy41NCAwIDAgMC0uMDc0LS43MzQgMi4wNDcgMi4wNDcgMCAwIDAtLjIyOC0uNjExem0tLjQ3NiAxLjk1M2MtLjAzOS4xOC0uMDk1LjMyOC0uMTY4LjQ0NWEuNzU1Ljc1NSAwIDAgMS0uMjY0LjI2Ni42ODcuNjg3IDAgMCAxLS42NTEuMDE1Ljc2Ljc2IDAgMCAxLS4yMzctLjIwNy45ODguOTg4IDAgMCAxLS4xNTQtLjMwNiAxLjI2MiAxLjI2MiAwIDAgMS0uMDU3LS4zODF2LS41MDZjMC0uMTcuMDItLjMyNi4wNjEtLjQ2NXMuMDk2LS4yNTguMTY4LS4zNTlhLjc1Ni43NTYgMCAwIDEgLjI1Ny0uMjMyYy4xLS4wNTUuMjEtLjA4Mi4zMzEtLjA4MmEuNjQ2LjY0NiAwIDAgMSAuNTcxLjMyYy4wNjYuMTA1LjExNi4yMy4xNS4zNzcuMDM1LjE0Ni4wNTIuMzEuMDUyLjQ5NCAwIC4yMzQtLjAxOS40NDEtLjA1OS42MjF6bTMuNjcyLTIuMzMyYS43LjcgMCAwIDEgLjEwNi4wNjZ2LjgxNGExLjE3OCAxLjE3OCAwIDAgMC0uMjczLS4yMjMuNjQ1LjY0NSAwIDAgMC0uMzE3LS4wODFjLS4wODUgMC0uMTYxLjAzMi0uMjM4LjA2NC0uMjYzLjE4MS0uNDY5LjU4Ni0uNDY5IDEuMzAxIDAgLjY2OC4xODIgMS4wMTEuNDIzIDEuMTQ2LjA4NC4wNC4xNzEuMDc0LjI3NC4wNzQuMDQ5IDAgLjEwMS0uMDEuMTUzLS4wMjdhLjg1Ni44NTYgMCAwIDAgLjE1OC0uMDY4IDEuMTYgMS4xNiAwIDAgMCAuMjg4LS4yMjV2Ljc3Yy0uMDkuMDc2LS4xOTIuMTM5LS4zMDkuMTg0YTEuMDk4IDEuMDk4IDAgMCAxLS40MTIuMDY4Ljk3NC45NzQgMCAwIDEtLjUyMy0uMTQzIDEuMjU3IDEuMjU3IDAgMCAxLS4zOTYtLjM5NiAyLjA5OCAyLjA5OCAwIDAgMS0uMjUyLS42MDIgMy4xMTggMy4xMTggMCAwIDEtLjA4OC0uNzU0YzAtLjMxNi4wMzItLjYwNC4wOTYtLjg2MS4wNjMtLjI1OC4xNTUtLjQ3OS4yNzMtLjY2LjExOS0uMTgyLjI2NS0uMzIyLjQzMy0uNDI0YTEuMTAyIDEuMTAyIDAgMCAxIDEuMDczLS4wMjN6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.color { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLXJlZHtmaWxsOiNlNTE0MDB9Lmljb24tdnMteWVsbG93e2ZpbGw6I2ZmY2MwMH0uaWNvbi12cy1ncmVlbntmaWxsOiMzMzk5MzN9Lmljb24tdnMtYmx1ZXtmaWxsOiMxYmExZTJ9Lmljb24tdnMtYWN0aW9uLXB1cnBsZXtmaWxsOiM2NTJkOTB9Lmljb24td2hpdGV7ZmlsbDojZmZmZmZmfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDhjMCA0LjQxMS0zLjU4OSA4LTggOGEyLjgwMyAyLjgwMyAwIDAgMS0yLjgtMi44YzAtLjgzMy4yNzItMS42MjkuNzY2LTIuMjQxYS41OTYuNTk2IDAgMCAwIC4xMDEtLjM1OS42NjcuNjY3IDAgMCAwLS42NjctLjY2Ni41OC41OCAwIDAgMC0uMzU4LjEwMkEzLjU4NCAzLjU4NCAwIDAgMSAyLjggMTAuOCAyLjgwMyAyLjgwMyAwIDAgMSAwIDhjMC00LjQxMSAzLjU4OS04IDgtOHM4IDMuNTg5IDggOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24td2hpdGUiIGQ9Ik01LjQgNy45MzNhMi42NyAyLjY3IDAgMCAxIDIuNjY3IDIuNjY2YzAgLjYwNi0uMTkzIDEuMTc5LS41NDQgMS42MTRhMS41OTkgMS41OTkgMCAwIDAtLjMyMy45ODcuOC44IDAgMCAwIC44LjhjMy4zMDkgMCA2LTIuNjkxIDYtNnMtMi42OTEtNi02LTYtNiAyLjY5MS02IDZjMCAuNDQxLjM1OS44LjguOC4zNzggMCAuNzI5LS4xMTQuOTg2LS4zMjJBMi41NjggMi41NjggMCAwIDEgNS40IDcuOTMzeiIgaWQ9Imljb25GZyIvPjxnIGlkPSJpY29uQmciPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNOCAxNWMtLjk5MiAwLTEuOC0uODA4LTEuOC0xLjggMC0uNjA2LjE5My0xLjE3OS41NDQtMS42MTMuMjA4LS4yNTkuMzIzLS42MDkuMzIzLS45ODcgMC0uOTE5LS43NDgtMS42NjYtMS42NjctMS42NjYtLjM3NyAwLS43MjguMTE1LS45ODYuMzIzQTIuNTggMi41OCAwIDAgMSAyLjggOS44QzEuODA4IDkuOCAxIDguOTkyIDEgOGMwLTMuODYgMy4xNC03IDctNyAzLjg1OSAwIDcgMy4xNCA3IDcgMCAzLjg1OS0zLjE0MSA3LTcgN3pNNS40IDcuOTMzYTIuNjcgMi42NyAwIDAgMSAyLjY2NyAyLjY2NmMwIC42MDYtLjE5MyAxLjE3OS0uNTQ0IDEuNjE0YTEuNTk5IDEuNTk5IDAgMCAwLS4zMjMuOTg3LjguOCAwIDAgMCAuOC44YzMuMzA5IDAgNi0yLjY5MSA2LTZzLTIuNjkxLTYtNi02LTYgMi42OTEtNiA2YzAgLjQ0MS4zNTkuOC44LjguMzc4IDAgLjcyOS0uMTE0Ljk4Ni0uMzIyQTIuNTY4IDIuNTY4IDAgMCAxIDUuNCA3LjkzM3oiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tcHVycGxlIiBkPSJNNC41IDUuMzc1YS44NzUuODc1IDAgMSAwIDAgMS43NS44NzUuODc1IDAgMCAwIDAtMS43NXoiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1ibHVlIiBkPSJNNy4xMjUgMy42MjVhLjg3NS44NzUgMCAxIDAgMCAxLjc1Ljg3NS44NzUgMCAwIDAgMC0xLjc1eiIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWdyZWVuIiBkPSJNMTAuNjI1IDQuNWEuODc1Ljg3NSAwIDEgMCAwIDEuNzUuODc1Ljg3NSAwIDAgMCAwLTEuNzV6Ii8+PHBhdGggY2xhc3M9Imljb24tdnMteWVsbG93IiBkPSJNMTEuNSA4YS44NzUuODc1IDAgMSAwIDAgMS43NS44NzUuODc1IDAgMCAwIDAtMS43NXoiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1yZWQiIGQ9Ik05Ljc1IDEwLjYyNWEuODc1Ljg3NSAwIDEgMCAwIDEuNzUuODc1Ljg3NSAwIDAgMCAwLTEuNzV6Ii8+PC9nPjwvc3ZnPg=="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.file { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNSAxNkgyVjBoOC42MjFMMTUgNC4zNzlWMTZ6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNMTMgMTRINFYyaDV2NGg0djh6bS0zLTlWMi4yMDdMMTIuNzkzIDVIMTB6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0zIDF2MTRoMTFWNC43OTNMMTAuMjA3IDFIM3ptMTAgMTNINFYyaDV2NGg0djh6bS0zLTlWMi4yMDdMMTIuNzkzIDVIMTB6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.reference { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojZjZmNmY2fS5pY29uLXZzLW91dHtmaWxsOiNmNmY2ZjZ9Lmljb24tdnMtYmd7ZmlsbDojNDI0MjQyfS5pY29uLXZzLWZne2ZpbGw6I2YwZWZmMX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiMwMDUzOWN9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTQgNC41NTZWMTNjMCAuOTctLjcwMSAyLTIgMkg0Yy0uOTcgMC0yLS43MDEtMi0yVjYuNjQ5QTMuNDk1IDMuNDk1IDAgMCAxIDAgMy41QzAgMS41NyAxLjU3IDAgMy41IDBINXYxaDUuMDYxTDE0IDQuNTU2eiIgaWQ9Im91dGxpbmUiIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMTMgNXY4cy0uMDM1IDEtMS4wMzUgMWgtOFMzIDE0IDMgMTNWOWgxdjRoOFY2SDkuMzk3bC41MTctLjUyTDkgNC41NzJWM0g3LjQxOUw2LjQxMyAyaDMuMjI4TDEzIDV6IiBpZD0iaWNvbkJnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik03LjQxOSAzSDl2MS41NzJMNy40MTkgM3ptMS45NzggM0w2LjQxNiA5SDR2NGg4VjZIOS4zOTd6IiBpZD0iaWNvbkZnIiBzdHlsZT0iZGlzcGxheTogbm9uZTsiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tYmx1ZSIgZD0iTTUuOTg4IDZIMy41YTIuNSAyLjUgMCAxIDEgMC01SDR2MWgtLjVDMi42NzMgMiAyIDIuNjczIDIgMy41UzIuNjczIDUgMy41IDVoMi41MTNMNCAzaDJsMi41IDIuNDg0TDYgOEg0bDEuOTg4LTJ6IiBpZD0iY29sb3JBY3Rpb24iLz48L3N2Zz4="); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.snippet { background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0ic3ZnNDY5NCIKICAgdmlld0JveD0iMCAwIDE2IDE2Ij4KICA8bWV0YWRhdGEKICAgICBpZD0ibWV0YWRhdGE0NzA1Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZGVmcwogICAgIGlkPSJkZWZzNDcwMyIgLz4KICA8c3R5bGUKICAgICBpZD0ic3R5bGU0Njk2Ij4uaWNvbi1jYW52YXMtdHJhbnNwYXJlbnR7b3BhY2l0eTowO2ZpbGw6I2Y2ZjZmNn0uaWNvbi12cy1vdXR7ZmlsbDojZjZmNmY2fS5pY29uLXZzLWFjdGlvbi1vcmFuZ2V7ZmlsbDojYzI3ZDFhfTwvc3R5bGU+CiAgPGcKICAgICBpZD0iZzQ3MDciCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMS4zMzMzMzMzLDAsMCwxLjMzMzMzMzMsLTI0NS45OTk5OSwtNS4zMzMzMzMpIj4KICAgIDxwYXRoCiAgICAgICBkPSJtIDE4NSw0IDExLDAgMCwxMiAtMTEsMCB6IgogICAgICAgaWQ9InBhdGg0NTM0IgogICAgICAgc3R5bGU9ImZpbGw6I2Y2ZjZmNiIgLz4KICAgIDxwYXRoCiAgICAgICBkPSJtIDE5NCwxMyAwLC03IC03LDAgMCw3IC0xLDAgMCwtOCA5LDAgMCw4IC0xLDAgeiBtIC03LDIgLTEsMCAwLC0xIDEsMCAwLDEgeiBtIDIsLTEgLTEsMCAwLDEgMSwwIDAsLTEgeiBtIDIsMCAtMSwwIDAsMSAxLDAgMCwtMSB6IG0gMiwxIC0xLDAgMCwtMSAxLDAgMCwxIHogbSAyLC0xIC0xLDAgMCwxIDEsMCAwLC0xIHoiCiAgICAgICBpZD0icGF0aDQ1MzYiCiAgICAgICBzdHlsZT0iZmlsbDojNDI0MjQyIiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gMTg3LDEzIDAsLTcgNywwIDAsNyAtNywwIHoiCiAgICAgICBpZD0icGF0aDQ1MzgiCiAgICAgICBzdHlsZT0iZmlsbDojZjBlZmYxIiAvPgogIDwvZz4KICA8cGF0aAogICAgIGlkPSJjYW52YXMiCiAgICAgZD0iTTE2IDE2SDBWMGgxNnYxNnoiCiAgICAgY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiAvPgo8L3N2Zz4K"); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor { background-image: none; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.folder { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uaWNvbi1jYW52YXMtdHJhbnNwYXJlbnR7b3BhY2l0eTowO2ZpbGw6I0Y2RjZGNjt9IC5pY29uLXZzLW91dHtvcGFjaXR5OjA7ZmlsbDojRjZGNkY2O30gLmljb24tdnMtZmd7ZmlsbDojRjBFRkYxO30gLmljb24tZm9sZGVye2ZpbGw6IzY1NjU2NTt9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNmgtMTZ2LTE2aDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDIuNXYxMGMwIC44MjctLjY3MyAxLjUtMS41IDEuNWgtMTEuOTk2Yy0uODI3IDAtMS41LS42NzMtMS41LTEuNXYtOGMwLS44MjcuNjczLTEuNSAxLjUtMS41aDIuODg2bDEtMmg4LjExYy44MjcgMCAxLjUuNjczIDEuNSAxLjV6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLWZvbGRlciIgZD0iTTE0LjUgMmgtNy40OTJsLTEgMmgtMy41MDRjLS4yNzcgMC0uNS4yMjQtLjUuNXY4YzAgLjI3Ni4yMjMuNS41LjVoMTEuOTk2Yy4yNzUgMCAuNS0uMjI0LjUtLjV2LTEwYzAtLjI3Ni0uMjI1LS41LS41LS41em0tLjQ5NiAyaC02LjQ5NmwuNS0xaDUuOTk2djF6IiBpZD0iaWNvbkJnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0xNCAzdjFoLTYuNWwuNS0xaDZ6IiBpZD0iaWNvbkZnIi8+PC9zdmc+"); }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor .colorspan {
	margin: 0 0 0 0.3em;
	border: 0.1em solid #000;
	width: 0.7em;
	height: 0.7em;
	display: inline-block;
}

/** Styles for the docs of the completion item in focus **/
.monaco-editor .suggest-widget .details {
	display: flex;
	flex-direction: column;
	cursor: default;
}

.monaco-editor .suggest-widget .details.no-docs {
	display: none;
}

.monaco-editor .suggest-widget.docs-below .details {
	border-top-width: 0px;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element {
	flex: 1;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body {
	position: absolute;
	box-sizing: border-box;
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .type {
	flex: 2;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
	word-break: break-all;
	margin: 0;
	padding: 4px 0 4px 5px;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs {
	margin: 0;
	padding: 4px 5px;
	white-space: pre-wrap;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs {
	white-space: initial;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs .code {
	white-space: pre-wrap;
	word-wrap: break-word;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > p:empty {
	display: none;
}

.monaco-editor .suggest-widget .details code {
	border-radius: 3px;
	padding: 0 0.4em;
}

/* High Contrast and Dark Theming */

.monaco-editor.vs-dark .suggest-widget .details > .monaco-scrollable-element > .body > .header > .close,
.monaco-editor.hc-black .suggest-widget .details > .monaco-scrollable-element > .body > .header > .close {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMyAzIDE2IDE2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDMgMyAxNiAxNiI+PHBvbHlnb24gZmlsbD0iI2U4ZThlOCIgcG9pbnRzPSIxMi41OTcsMTEuMDQyIDE1LjQsMTMuODQ1IDEzLjg0NCwxNS40IDExLjA0MiwxMi41OTggOC4yMzksMTUuNCA2LjY4MywxMy44NDUgOS40ODUsMTEuMDQyIDYuNjgzLDguMjM5IDguMjM4LDYuNjgzIDExLjA0Miw5LjQ4NiAxMy44NDUsNi42ODMgMTUuNCw4LjIzOSIvPjwvc3ZnPg==");
}

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDEwYzAgMi4yMDUtMS43OTQgNC00IDQtMS44NTggMC0zLjQxMS0xLjI3OS0zLjg1OC0zaC0uOTc4bDIuMzE4IDRIMHYtMS43MDNsMi0zLjQwOFYwaDExdjYuMTQyYzEuNzIxLjQ0NyAzIDIgMyAzLjg1OHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0xMiAxdjQuNzVBNC4yNTUgNC4yNTUgMCAwIDAgNy43NSAxMGgtLjczMkw0LjI3NSA1LjI2OSAzIDcuNDQyVjFoOXpNNy43NDcgMTRMNC4yNjkgOCAuNzQ4IDE0aDYuOTk5ek0xNSAxMGEzIDMgMCAxIDEtNiAwIDMgMyAwIDAgMSA2IDB6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.method,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.method,
.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.function,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.function,
.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.constructor,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.constructor { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1wdXJwbGV7ZmlsbDojYjE4MGQ3fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE1IDMuMzQ5djguNDAzTDguOTc1IDE2SDguMDdMMSAxMS41ODJWMy4zMjdMNy41OTUgMGgxLjExOEwxNSAzLjM0OXoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0xMi43MTUgNC4zOThMOC40ODcgNy4wMiAzLjU2NSA0LjI3Mmw0LjU3OC0yLjMwOSA0LjU3MiAyLjQzNXpNMyA1LjEwMmw1IDIuNzkydjUuNzA1bC01LTMuMTI1VjUuMTAyem02IDguNDM0VjcuODc4bDQtMi40OHY1LjMxN2wtNCAyLjgyMXoiIGlkPSJpY29uRmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tcHVycGxlIiBkPSJNOC4xNTYuODM3TDIgMy45NDJ2Ny4wODVMOC41MTcgMTUuMSAxNCAxMS4yMzNWMy45NUw4LjE1Ni44Mzd6bTQuNTU5IDMuNTYxTDguNDg3IDcuMDIgMy41NjUgNC4yNzJsNC41NzgtMi4zMDkgNC41NzIgMi40MzV6TTMgNS4xMDJsNSAyLjc5MnY1LjcwNWwtNS0zLjEyNVY1LjEwMnptNiA4LjQzNFY3Ljg3OGw0LTIuNDh2NS4zMTdsLTQgMi44MjF6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.field,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.field { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6Izc1YmVmZn08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0wIDEwLjczNlY0LjVMOSAwbDcgMy41djYuMjM2bC05IDQuNS03LTMuNXoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik05IDFMMSA1djVsNiAzIDgtNFY0TDkgMXpNNyA2Ljg4MkwzLjIzNiA1IDkgMi4xMTggMTIuNzY0IDQgNyA2Ljg4MnoiIGlkPSJpY29uQmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTkgMi4xMThMMTIuNzY0IDQgNyA2Ljg4MiAzLjIzNiA1IDkgMi4xMTh6IiBpZD0iaWNvbkZnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.event,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.event { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYWN0aW9uLW9yYW5nZXtmaWxsOiNlOGFiNTN9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTQgMS40MTRMOS40MTQgNkgxNHYxLjQxNEw1LjQxNCAxNkgzdi0xLjIzNEw1LjM3MSAxMEgyVjguNzY0TDYuMzgyIDBIMTR2MS40MTR6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLW9yYW5nZSIgZD0iTTcgN2g2bC04IDhINGwyLjk4NS02SDNsNC04aDZMNyA3eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.operator,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.operator { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6Izc1YmVmZn08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xIDF2MTRoMTRWMUgxem02IDEySDN2LTFoNHYxem0wLTNIM1Y5aDR2MXptMC01SDV2Mkg0VjVIMlY0aDJWMmgxdjJoMnYxem0zLjI4MSA4SDguNzE5bDMtNGgxLjU2M2wtMy4wMDEgNHpNMTQgNUg5VjRoNXYxeiIgaWQ9Imljb25CZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNNyA1SDV2Mkg0VjVIMlY0aDJWMmgxdjJoMnYxem03LTFIOXYxaDVWNHpNNyA5SDN2MWg0Vjl6bTAgM0gzdjFoNHYtMXptMy4yODEgMWwzLTRoLTEuNTYzbC0zIDRoMS41NjN6IiBpZD0iaWNvbkZnIiBzdHlsZT0iZGlzcGxheTogbm9uZTsiLz48L3N2Zz4="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.variable,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.variable { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiM3NWJlZmZ9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTEgM3YxLjAxNUw4LjczMyAyLjg4MiA1IDQuNzQ5VjNIMHYxMGg1di0xLjg1OWwyLjE1NiAxLjA3N0wxMSAxMC4yOTVWMTNoNVYzaC01eiIgaWQ9Im91dGxpbmUiIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMiA1djZoMnYxSDFWNGgzdjFIMnptMTAgNnYxaDNWNGgtM3YxaDJ2NmgtMnoiIGlkPSJpY29uQmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTcuMTU2IDcuMTU2bC0xLjU3OC0uNzg5IDMuMTU2LTEuNTc4IDEuNTc4Ljc4OS0zLjE1NiAxLjU3OHoiIGlkPSJpY29uRmciIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWFjdGlvbi1ibHVlIiBkPSJNOC43MzMgNEw0IDYuMzY3djMuMTU2TDcuMTU2IDExLjFsNC43MzMtMi4zNjdWNS41NzhMOC43MzMgNHpNNy4xNTYgNy4xNTZsLTEuNTc4LS43ODkgMy4xNTYtMS41NzggMS41NzguNzg5LTMuMTU2IDEuNTc4eiIgaWQ9ImNvbG9ySW1wb3J0YW5jZSIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.class,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.class { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYWN0aW9uLW9yYW5nZXtmaWxsOiNlOGFiNTN9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTYgNi41ODZsLTMtM0wxMS41ODYgNUg5LjQxNGwxLTEtNC00aC0uODI4TDAgNS41ODZ2LjgyOGw0IDRMNi40MTQgOEg3djVoMS41ODZsMyAzaC44MjhMMTYgMTIuNDE0di0uODI4TDEzLjkxNCA5LjUgMTYgNy40MTR2LS44Mjh6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWFjdGlvbi1vcmFuZ2UiIGQ9Ik0xMyAxMGwyIDItMyAzLTItMiAxLTFIOFY3SDZMNCA5IDEgNmw1LTUgMyAzLTIgMmg1bDEtMSAyIDItMyAzLTItMiAxLTFIOXY0bDIuOTk5LjAwMkwxMyAxMHoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.interface,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.interface { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6Izc1YmVmZn08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xMS41IDEyYy0xLjkxNSAwLTMuNjAyLTEuMjQxLTQuMjI4LTNoLTEuNDFhMy4xMSAzLjExIDAgMCAxLTIuNzM3IDEuNjI1QzEuNDAyIDEwLjYyNSAwIDkuMjIzIDAgNy41czEuNDAyLTMuMTI1IDMuMTI1LTMuMTI1YzEuMTY1IDAgMi4yMDEuNjM5IDIuNzM3IDEuNjI1aDEuNDFjLjYyNi0xLjc1OSAyLjMxMy0zIDQuMjI4LTNDMTMuOTgxIDMgMTYgNS4wMTkgMTYgNy41UzEzLjk4MSAxMiAxMS41IDEyeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTExLjUgOUExLjUwMSAxLjUwMSAwIDEgMSAxMyA3LjVjMCAuODI2LS42NzMgMS41LTEuNSAxLjV6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMS41IDRhMy40OSAzLjQ5IDAgMCAwLTMuNDUgM0g1LjE4NUEyLjEyMiAyLjEyMiAwIDAgMCAxIDcuNWEyLjEyMyAyLjEyMyAwIDEgMCA0LjE4NS41SDguMDVhMy40OSAzLjQ5IDAgMCAwIDMuNDUgMyAzLjUgMy41IDAgMSAwIDAtN3ptMCA1Yy0uODI3IDAtMS41LS42NzMtMS41LTEuNVMxMC42NzMgNiAxMS41IDZzMS41LjY3MyAxLjUgMS41UzEyLjMyNyA5IDExLjUgOXoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.struct,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.struct { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYWN0aW9uLWJsdWV7ZmlsbDojNzViZWZmfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTkgMTRWOEg3djZIMVYyaDE0djEySDl6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMCA5aDR2NGgtNFY5em0tOCA0aDRWOUgydjR6TTIgM3Y0aDEyVjNIMnoiIGlkPSJpY29uQmciLz48L3N2Zz4="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.type-parameter,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.type-parameter { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTEwLjcwMiAxMC41bDItMi0yLTIgLjUtLjVIMTB2NWgxdjNINXYtM2gxVjZINC43OThsLjUuNS0yIDIgMiAyTDMgMTIuNzk3bC0zLTNWNy4yMDFsMy0zVjJoMTB2Mi4yMDFsMyAzdjIuNTk2bC0zIDMtMi4yOTgtMi4yOTd6IiBpZD0ib3V0bGluZSIgc3R5bGU9ImRpc3BsYXk6IG5vbmU7Ii8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik00IDNoOHYyaC0xdi0uNWMwLS4yNzctLjIyNC0uNS0uNS0uNUg5djcuNWMwIC4yNzUuMjI0LjUuNS41aC41djFINnYtMWguNWEuNS41IDAgMCAwIC41LS41VjRINS41YS41LjUgMCAwIDAtLjUuNVY1SDRWM3pNMyA1LjYxNUwuMTE2IDguNSAzIDExLjM4M2wuODg0LS44ODMtMi0yIDItMkwzIDUuNjE1em0xMCAwbC0uODg0Ljg4NSAyIDItMiAyIC44ODQuODgzTDE1Ljg4NCA4LjUgMTMgNS42MTV6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.module,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.module { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTkuMjYgMTEuOTg0bC45NzgtLjAyMWEuOTYyLjk2MiAwIDAgMCAuMDktLjAwNmMuMDExLS4wNjMuMDI2LS4xNzkuMDI2LS4zNjFWOS42ODhjMC0uNjc5LjE4NS0xLjI1Ny41My0xLjcwNy0uMzQ2LS40NTItLjUzLTEuMDMtLjUzLTEuNzA1VjQuMzVjMC0uMTY3LS4wMjEtLjI1OS0uMDM0LS4zMDJMOS4yNiA0LjAyVi45NzNsMS4wMTEuMDExYzIuMTY3LjAyNCAzLjQwOSAxLjE1NiAzLjQwOSAzLjEwNXYxLjk2MmMwIC4zNTEuMDcxLjQ2MS4wNzIuNDYybC45MzYuMDYuMDUzLjkyN3YxLjkzNmwtLjkzNi4wNjFjLS4wNzYuMDE2LS4xMjUuMTQ2LS4xMjUuNDI0djIuMDE3YzAgLjkxNC0uMzMyIDMuMDQzLTMuNDA4IDMuMDc4bC0xLjAxMi4wMTF2LTMuMDQzem0tMy41MjEgMy4wMzJjLTMuMDg5LS4wMzUtMy40MjItMi4xNjQtMy40MjItMy4wNzhWOS45MjFjMC0uMzI3LS4wNjYtLjQzMi0uMDY3LS40MzNsLS45MzctLjA2LS4wNjMtLjkyOVY2LjU2M2wuOTQyLS4wNmMuMDU4IDAgLjEyNS0uMTE0LjEyNS0uNDUyVjQuMDljMC0xLjk0OSAxLjI0OC0zLjA4MSAzLjQyMi0zLjEwNUw2Ljc1Ljk3M1Y0LjAybC0uOTc1LjAyM2EuNTcyLjU3MiAwIDAgMC0uMDkzLjAxYy4wMDYuMDIxLS4wMTkuMTE1LS4wMTkuMjk3djEuOTI4YzAgLjY3NS0uMTg2IDEuMjUzLS41MzQgMS43MDUuMzQ4LjQ1LjUzNCAxLjAyOC41MzQgMS43MDd2MS45MDdjMCAuMTc1LjAxNC4yOTEuMDI3LjM2My4wMjMuMDAyIDEuMDYuMDI1IDEuMDYuMDI1djMuMDQzbC0xLjAxMS0uMDEyeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTUuNzUgMTQuMDE2Yy0xLjYyMy0uMDE5LTIuNDM0LS43MTEtMi40MzQtMi4wNzhWOS45MjFjMC0uOTAyLS4zNTUtMS4zNzYtMS4wNjYtMS40MjJ2LS45OThjLjcxMS0uMDQ1IDEuMDY2LS41MjkgMS4wNjYtMS40NDlWNC4wOWMwLTEuMzg1LjgxMS0yLjA4NyAyLjQzNC0yLjEwNXYxLjA2Yy0uNzI1LjAxNy0xLjA4Ny40NTMtMS4wODcgMS4zMDV2MS45MjhjMCAuOTItLjQ1NCAxLjQ4OC0xLjM2IDEuNzAyVjhjLjkwNy4yMDEgMS4zNi43NjMgMS4zNiAxLjY4OHYxLjkwN2MwIC40ODguMDgxLjgzNS4yNDMgMS4wNDIuMTYyLjIwOC40NDMuMzE2Ljg0NC4zMjV2MS4wNTR6bTcuOTktNS41MTdjLS43MDYuMDQ1LTEuMDYuNTItMS4wNiAxLjQyMnYyLjAxN2MwIDEuMzY3LS44MDcgMi4wNi0yLjQyIDIuMDc4di0xLjA1M2MuMzk2LS4wMDkuNjc4LS4xMTguODQ0LS4zMjguMTY3LS4yMS4yNS0uNTU2LjI1LTEuMDM5VjkuNjg4YzAtLjkyNS40NDktMS40ODggMS4zNDctMS42ODh2LS4wMjFjLS44OTgtLjIxNC0xLjM0Ny0uNzgyLTEuMzQ3LTEuNzAyVjQuMzVjMC0uODUyLS4zNjQtMS4yODgtMS4wOTQtMS4zMDZ2LTEuMDZjMS42MTMuMDE4IDIuNDIuNzIgMi40MiAyLjEwNXYxLjk2MmMwIC45Mi4zNTQgMS40MDQgMS4wNiAxLjQ0OXYuOTk5eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.property,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.property { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDUuNWE1LjUgNS41IDAgMCAxLTUuNSA1LjVjLS4yNzUgMC0uNTQzLS4wMjctLjgwNy0uMDY2bC0uMDc5LS4wMTJhNS40MjkgNS40MjkgMCAwIDEtLjgxLS4xOTJsLTQuNTM3IDQuNTM3Yy0uNDcyLjQ3My0xLjEuNzMzLTEuNzY3LjczM3MtMS4yOTUtLjI2LTEuNzY4LS43MzJhMi41MDIgMi41MDIgMCAwIDEgMC0zLjUzNWw0LjUzNy00LjUzN2E1LjQ1MiA1LjQ1MiAwIDAgMS0uMTkxLS44MTJjLS4wMDUtLjAyNS0uMDA4LS4wNTEtLjAxMi0uMDc3QTUuNTAzIDUuNTAzIDAgMCAxIDUgNS41YTUuNSA1LjUgMCAxIDEgMTEgMHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0xNSA1LjVhNC41IDQuNSAwIDAgMS00LjUgNC41Yy0uNjkzIDAtMS4zNDItLjE3LTEuOTI5LS40NWwtNS4wMSA1LjAxYy0uMjkzLjI5NC0uNjc3LjQ0LTEuMDYxLjQ0cy0uNzY4LS4xNDYtMS4wNjEtLjQzOWExLjUgMS41IDAgMCAxIDAtMi4xMjFsNS4wMS01LjAxQTQuNDgzIDQuNDgzIDAgMCAxIDYgNS41IDQuNSA0LjUgMCAwIDEgMTAuNSAxYy42OTMgMCAxLjM0Mi4xNyAxLjkyOS40NUw5LjYzNiA0LjI0M2wyLjEyMSAyLjEyMSAyLjc5My0yLjc5M2MuMjguNTg3LjQ1IDEuMjM2LjQ1IDEuOTI5eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.unit,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.unit { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxMS4wMTNIMVY0aDE1djcuMDEzeiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTggOUg3VjZoM3YzSDlWN0g4djJ6TTQgN2gxdjJoMVY2SDN2M2gxVjd6bTggMGgxdjJoMVY2aC0zdjNoMVY3eiIgaWQ9Imljb25GZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMiA1djVoMTNWNUgyem00IDRINVY3SDR2MkgzVjZoM3Yzem00IDBIOVY3SDh2Mkg3VjZoM3Yzem00IDBoLTFWN2gtMXYyaC0xVjZoM3YzeiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.constant,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.constant { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMjUyNTI2fS5pY29uLXZzLW91dHtmaWxsOiMyNTI1MjZ9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiM3NWJlZmZ9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMi44NzkgMTRMMSAxMi4xMjFWMy44NzlMMi44NzkgMmgxMC4yNDJMMTUgMy44Nzl2OC4yNDJMMTMuMTIxIDE0SDIuODc5eiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1mZyIgZD0iTTEyLjI5MyA0SDMuNzA3TDMgNC43MDd2Ni41ODZsLjcwNy43MDdoOC41ODZsLjcwNy0uNzA3VjQuNzA3TDEyLjI5MyA0ek0xMSAxMEg1VjloNnYxem0wLTNINVY2aDZ2MXoiIGlkPSJpY29uRmciLz48ZyBpZD0iaWNvbkJnIj48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTEyLjcwNyAxM0gzLjI5M0wyIDExLjcwN1Y0LjI5M0wzLjI5MyAzaDkuNDE0TDE0IDQuMjkzdjcuNDE0TDEyLjcwNyAxM3ptLTktMWg4LjU4NmwuNzA3LS43MDdWNC43MDdMMTIuMjkzIDRIMy43MDdMMyA0LjcwN3Y2LjU4NmwuNzA3LjcwN3oiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tYmx1ZSIgZD0iTTExIDdINVY2aDZ2MXptMCAySDV2MWg2Vjl6Ii8+PC9nPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.value,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.value,
.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.enum,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.enum { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1vcmFuZ2V7ZmlsbDojZThhYjUzfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE0LjQxNCAxTDE2IDIuNTg2djUuODI4TDE0LjQxNCAxMEgxMHYzLjQxNkw4LjQxNCAxNUgxLjU4NkwwIDEzLjQxNnYtNS44M0wxLjU4NiA2SDZWMi41ODZMNy41ODYgMWg2LjgyOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0yIDEzaDZWOEgydjV6bTEtNGg0djFIM1Y5em0wIDJoNHYxSDN2LTF6bTExLTVWM0g4djNoLjQxNEw5IDYuNTg2VjZoNHYxSDkuNDE0bC41ODYuNTg2VjhoNFY2em0tMS0xSDlWNGg0djF6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLW9yYW5nZSIgZD0iTTMgMTFoNC4wMDF2MUgzdi0xem0wLTFoNC4wMDFWOUgzdjF6bTYtMnY1bC0xIDFIMmwtMS0xVjhsMS0xaDZsMSAxek04IDhIMnY1aDZWOHptMS0ybDEgMWgzVjZIOXptMC0xaDRWNEg5djF6bTUtM0g4TDcgM3YzaDFWM2g2djVoLTR2MWg0bDEtMVYzbC0xLTF6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.enum-member,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.enum-member { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtZmd7ZmlsbDojMmIyODJlfS5pY29uLXZzLWFjdGlvbi1ibHVle2ZpbGw6Izc1YmVmZn08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0wIDE1VjZoNlYyLjU4Nkw3LjU4NSAxaDYuODI5TDE2IDIuNTg2djUuODI5TDE0LjQxNCAxMEgxMHY1SDB6bTMtNnoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik04IDN2M2g1djFoLTN2MWg0VjNIOHptNSAySDlWNGg0djF6TTIgOHY1aDZWOEgyem01IDNIM3YtMWg0djF6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYWN0aW9uLWJsdWUiIGQ9Ik0xMCA2aDN2MWgtM1Y2ek05IDR2MWg0VjRIOXptNS0ySDhMNyAzdjNoMVYzaDZ2NWgtNHYxaDRsMS0xVjNsLTEtMXptLTcgOEgzdjFoNHYtMXptMi0zdjdIMVY3aDh6TTggOEgydjVoNlY4eiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.keyword,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.keyword { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiA1VjJIOVYxSDB2MTRoMTN2LTNoM1Y5aC0xVjZIOVY1aDd6bS04IDdWOWgxdjNIOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik0yIDNoNXYxSDJWM3oiIGlkPSJpY29uRmciLz48cGF0aCBjbGFzcz0iaWNvbi12cy1iZyIgZD0iTTE1IDRoLTVWM2g1djF6bS0xIDNoLTJ2MWgyVjd6bS00IDBIMXYxaDlWN3ptMiA2SDF2MWgxMXYtMXptLTUtM0gxdjFoNnYtMXptOCAwaC01djFoNXYtMXpNOCAydjNIMVYyaDd6TTcgM0gydjFoNVYzeiIgaWQ9Imljb25CZyIvPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.text,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.text { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAxNUgwVjFoMTZ2MTR6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNOS4yMjkgNy4zNTRjLjAzNS4xNDYuMDUyLjMxLjA1Mi40OTQgMCAuMjM0LS4wMi40NDEtLjA2LjYyMS0uMDM5LjE4LS4wOTUuMzI4LS4xNjguNDQ1YS42ODcuNjg3IDAgMCAxLS45MTQuMjgxLjc2Ljc2IDAgMCAxLS4yMzctLjIwNy45ODguOTg4IDAgMCAxLS4xNTQtLjMwNiAxLjI2MiAxLjI2MiAwIDAgMS0uMDU3LS4zODF2LS41MDZjMC0uMTcuMDItLjMyNi4wNjEtLjQ2NXMuMDk2LS4yNTguMTY4LS4zNTlhLjc1Ni43NTYgMCAwIDEgLjI1Ny0uMjMyYy4xLS4wNTUuMjEtLjA4Mi4zMzEtLjA4MmEuNjQ2LjY0NiAwIDAgMSAuNTcxLjMyYy4wNjcuMTA1LjExNi4yMy4xNS4zNzd6bS01LjEyNi44NjlhLjU1Ny41NTcgMCAwIDAtLjE5Ni4xMzJjLS4wNDcuMDUzLS4wOC4xMTItLjA5Ny4xOHMtLjAyOC4xNDctLjAyOC4yMzNhLjUxMy41MTMgMCAwIDAgLjE1Ny4zOS41MjguNTI4IDAgMCAwIC4xODYuMTEzLjY4Mi42ODIgMCAwIDAgLjI0Mi4wNDEuNzYuNzYgMCAwIDAgLjU5My0uMjcxLjg5Ny44OTcgMCAwIDAgLjE2NS0uMjk1Yy4wMzgtLjExMy4wNTktLjIzNC4wNTktLjM2NXYtLjM0NmwtLjc2MS4xMWExLjI5IDEuMjkgMCAwIDAtLjMyLjA3OHpNMTQgM3YxMEgyVjNoMTJ6TTUuOTYyIDcuNDY5YzAtLjIzOC0uMDI3LS40NTEtLjA4My0uNjM3YTEuMjg2IDEuMjg2IDAgMCAwLS4yNDktLjQ3MSAxLjA4IDEuMDggMCAwIDAtLjQyNC0uMjk1IDEuNjQ0IDEuNjQ0IDAgMCAwLS42MDgtLjEwMWMtLjExOSAwLS4yNDEuMDEyLS4zNjguMDMzYTMuMjEzIDMuMjEzIDAgMCAwLS42NzMuMTk1IDEuMzEzIDEuMzEzIDAgMCAwLS4yMTIuMTE0di43NjhjLjE1OC0uMTMyLjM0MS0uMjM1LjU0NC0uMzEzLjIwNC0uMDc4LjQxMy0uMTE3LjYyNy0uMTE3LjIxMyAwIC4zNzcuMDYzLjQ5NC4xODYuMTE2LjEyNS4xNzQuMzI0LjE3NC42bC0xLjAzLjE1NGMtLjIwNS4wMjYtLjM4LjA3Ny0uNTI2LjE1MWExLjA4MyAxLjA4MyAwIDAgMC0uNTYzLjY2QTEuNTYyIDEuNTYyIDAgMCAwIDMgOC44NTdjMCAuMTcuMDI1LjMyMy4wNzQuNDYzYS45NDUuOTQ1IDAgMCAwIC41NjguNTk2Yy4xMzkuMDU3LjI5Ny4wODQuNDc4LjA4NC4yMjkgMCAuNDMxLS4wNTMuNjA0LS4xNmExLjMgMS4zIDAgMCAwIC40MzktLjQ2M2guMDE0di41MjloLjc4NVY3LjQ2OXpNMTAgNy44NjFhMy41NCAzLjU0IDAgMCAwLS4wNzQtLjczNCAyLjA0NyAyLjA0NyAwIDAgMC0uMjI4LS42MTEgMS4yMDMgMS4yMDMgMCAwIDAtLjM5NC0uNDE2IDEuMDMgMS4wMyAwIDAgMC0uNTc0LS4xNTNjLS4xMjMgMC0uMjM0LjAxOC0uMzM2LjA1MWExIDEgMCAwIDAtLjI3OC4xNDcgMS4xNTMgMS4xNTMgMCAwIDAtLjIyNS4yMjIgMi4wMjIgMi4wMjIgMCAwIDAtLjE4MS4yODloLS4wMTNWNUg3djQuODg3aC42OTd2LS40ODVoLjAxM2MuMDQ0LjA4Mi4wOTUuMTU4LjE1MS4yMjkuMDU3LjA3LjExOS4xMzMuMTkxLjE4NmEuODM1LjgzNSAwIDAgMCAuMjM4LjEyMS45NDMuOTQzIDAgMCAwIC4yOTMuMDQyYy4yMyAwIC40MzQtLjA1My42MDktLjE2YTEuMzQgMS4zNCAwIDAgMCAuNDQzLS40NDNjLjEyLS4xODguMjExLS40MTIuMjcyLS42NzJBMy42MiAzLjYyIDAgMCAwIDEwIDcuODYxem0zLTEuNjU4YS43LjcgMCAwIDAtLjEwNi0uMDY2IDEuMTgzIDEuMTgzIDAgMCAwLS4xNDItLjA2MyAxLjIzMyAxLjIzMyAwIDAgMC0uMzYzLS4wNjVjLS4yMDkgMC0uMzk5LjA1MS0uNTY5LjE1YTEuMzU1IDEuMzU1IDAgMCAwLS40MzMuNDI0Yy0uMTE4LjE4Mi0uMjEuNDAyLS4yNzMuNjZhMy42MyAzLjYzIDAgMCAwLS4wMDggMS42MTVjLjA2LjIzLjE0My40My4yNTIuNjAyLjEwOS4xNjguMjQxLjMwMy4zOTYuMzk2YS45NzIuOTcyIDAgMCAwIC41MjQuMTQ0Yy4xNTggMCAuMjk2LS4wMjEuNDEzLS4wNjguMTE3LS4wNDUuMjE5LS4xMDguMzA5LS4xODR2LS43N2ExLjA5NCAxLjA5NCAwIDAgMS0uMjg4LjIyNS44MTkuODE5IDAgMCAxLS4xNTguMDY4LjQ4LjQ4IDAgMCAxLS4xNTMuMDI3LjYyLjYyIDAgMCAxLS4yNzQtLjA3NGMtLjI0MS0uMTM2LS40MjMtLjQ3OS0uNDIzLTEuMTQ2IDAtLjcxNS4yMDYtMS4xMi40NjktMS4zMDEuMDc3LS4wMzIuMTUzLS4wNjQuMjM4LS4wNjQuMTEzIDAgLjIyLjAyNy4zMTcuMDgyLjA5Ni4wNTcuMTg4LjEzMS4yNzIuMjIzdi0uODE1eiIgaWQ9Imljb25GZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMSAydjEyaDE0VjJIMXptMTMgMTFIMlYzaDEydjEwek01LjYzIDYuMzYxYTEuMDggMS4wOCAwIDAgMC0uNDI0LS4yOTUgMS42NDQgMS42NDQgMCAwIDAtLjYwOC0uMTAxYy0uMTE5IDAtLjI0MS4wMTItLjM2OC4wMzNhMy4yMTMgMy4yMTMgMCAwIDAtLjY3My4xOTUgMS4zMTMgMS4zMTMgMCAwIDAtLjIxMi4xMTR2Ljc2OGMuMTU4LS4xMzIuMzQxLS4yMzUuNTQ0LS4zMTMuMjA0LS4wNzguNDEzLS4xMTcuNjI3LS4xMTcuMjEzIDAgLjM3Ny4wNjMuNDk0LjE4Ni4xMTYuMTI1LjE3NC4zMjQuMTc0LjZsLTEuMDMuMTU0Yy0uMjA1LjAyNi0uMzguMDc3LS41MjYuMTUxYTEuMDgzIDEuMDgzIDAgMCAwLS41NjMuNjZBMS41NjIgMS41NjIgMCAwIDAgMyA4Ljg1N2MwIC4xNy4wMjUuMzIzLjA3NC40NjNhLjk0NS45NDUgMCAwIDAgLjU2OC41OTZjLjEzOS4wNTcuMjk3LjA4NC40NzguMDg0LjIyOSAwIC40MzEtLjA1My42MDQtLjE2YTEuMyAxLjMgMCAwIDAgLjQzOS0uNDYzaC4wMTR2LjUyOWguNzg1VjcuNDY5YzAtLjIzOC0uMDI3LS40NTEtLjA4My0uNjM3YTEuMjg2IDEuMjg2IDAgMCAwLS4yNDktLjQ3MXptLS40NDYgMi4wMmMwIC4xMzEtLjAyLjI1Mi0uMDU5LjM2NWEuODk3Ljg5NyAwIDAgMS0uMTY1LjI5NS43NTguNzU4IDAgMCAxLS41OTMuMjcyLjY4Mi42ODIgMCAwIDEtLjI0Mi0uMDQxLjUwNy41MDcgMCAwIDEtLjMwMi0uMjg2LjU4My41ODMgMCAwIDEtLjA0MS0uMjE4YzAtLjA4Ni4wMS0uMTY0LjAyNy0uMjMycy4wNTEtLjEyNy4wOTgtLjE4YS41NDYuNTQ2IDAgMCAxIC4xOTYtLjEzM2MuMDgzLS4wMzMuMTg5LS4wNjEuMzItLjA3OGwuNzYxLS4xMDl2LjM0NXptNC41MTQtMS44NjVhMS4yMDMgMS4yMDMgMCAwIDAtLjM5NC0uNDE2IDEuMDMgMS4wMyAwIDAgMC0uNTc0LS4xNTNjLS4xMjMgMC0uMjM0LjAxOC0uMzM2LjA1MWExIDEgMCAwIDAtLjI3OC4xNDcgMS4xNTMgMS4xNTMgMCAwIDAtLjIyNS4yMjIgMi4wMjIgMi4wMjIgMCAwIDAtLjE4MS4yODloLS4wMTNWNUg3djQuODg3aC42OTd2LS40ODVoLjAxM2MuMDQ0LjA4Mi4wOTUuMTU4LjE1MS4yMjkuMDU3LjA3LjExOS4xMzMuMTkxLjE4NmEuODM1LjgzNSAwIDAgMCAuMjM4LjEyMS45NDMuOTQzIDAgMCAwIC4yOTMuMDQyYy4yMyAwIC40MzQtLjA1My42MDktLjE2YTEuMzQgMS4zNCAwIDAgMCAuNDQzLS40NDNjLjEyLS4xODguMjExLS40MTIuMjcyLS42NzJBMy42MiAzLjYyIDAgMCAwIDEwIDcuODYxYTMuNTQgMy41NCAwIDAgMC0uMDc0LS43MzQgMi4wNDcgMi4wNDcgMCAwIDAtLjIyOC0uNjExem0tLjQ3NiAxLjk1M2MtLjAzOS4xOC0uMDk1LjMyOC0uMTY4LjQ0NWEuNzU1Ljc1NSAwIDAgMS0uMjY0LjI2Ni42ODcuNjg3IDAgMCAxLS42NTEuMDE1Ljc2Ljc2IDAgMCAxLS4yMzctLjIwNy45ODguOTg4IDAgMCAxLS4xNTQtLjMwNiAxLjI2MiAxLjI2MiAwIDAgMS0uMDU3LS4zODF2LS41MDZjMC0uMTcuMDItLjMyNi4wNjEtLjQ2NXMuMDk2LS4yNTguMTY4LS4zNTlhLjc1Ni43NTYgMCAwIDEgLjI1Ny0uMjMyYy4xLS4wNTUuMjEtLjA4Mi4zMzEtLjA4MmEuNjQ2LjY0NiAwIDAgMSAuNTcxLjMyYy4wNjYuMTA1LjExNi4yMy4xNS4zNzcuMDM1LjE0Ni4wNTIuMzEuMDUyLjQ5NCAwIC4yMzQtLjAxOS40NDEtLjA1OS42MjF6bTMuNjcyLTIuMzMyYS43LjcgMCAwIDEgLjEwNi4wNjZ2LjgxNGExLjE3OCAxLjE3OCAwIDAgMC0uMjczLS4yMjMuNjQ1LjY0NSAwIDAgMC0uMzE3LS4wODFjLS4wODUgMC0uMTYxLjAzMi0uMjM4LjA2NC0uMjYzLjE4MS0uNDY5LjU4Ni0uNDY5IDEuMzAxIDAgLjY2OC4xODIgMS4wMTEuNDIzIDEuMTQ2LjA4NC4wNC4xNzEuMDc0LjI3NC4wNzQuMDQ5IDAgLjEwMS0uMDEuMTUzLS4wMjdhLjg1Ni44NTYgMCAwIDAgLjE1OC0uMDY4IDEuMTYgMS4xNiAwIDAgMCAuMjg4LS4yMjV2Ljc3Yy0uMDkuMDc2LS4xOTIuMTM5LS4zMDkuMTg0YTEuMDk4IDEuMDk4IDAgMCAxLS40MTIuMDY4Ljk3NC45NzQgMCAwIDEtLjUyMy0uMTQzIDEuMjU3IDEuMjU3IDAgMCAxLS4zOTYtLjM5NiAyLjA5OCAyLjA5OCAwIDAgMS0uMjUyLS42MDIgMy4xMTggMy4xMTggMCAwIDEtLjA4OC0uNzU0YzAtLjMxNi4wMzItLjYwNC4wOTYtLjg2MS4wNjMtLjI1OC4xNTUtLjQ3OS4yNzMtLjY2LjExOS0uMTgyLjI2NS0uMzIyLjQzMy0uNDI0YTEuMTAyIDEuMTAyIDAgMCAxIDEuMDczLS4wMjN6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.color,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.color { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLXJlZHtmaWxsOiNmNDg3NzF9Lmljb24tdnMteWVsbG93e2ZpbGw6I2ZmY2MwMH0uaWNvbi12cy1ncmVlbntmaWxsOiMzMzk5MzN9Lmljb24tdnMtYmx1ZXtmaWxsOiMxYmExZTJ9Lmljb24tdnMtYWN0aW9uLXB1cnBsZXtmaWxsOiNiMTgwZDd9Lmljb24td2hpdGV7ZmlsbDojMDAwMDAwfTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZIMFYwaDE2djE2eiIgaWQ9ImNhbnZhcyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLW91dCIgZD0iTTE2IDhjMCA0LjQxMS0zLjU4OSA4LTggOGEyLjgwMyAyLjgwMyAwIDAgMS0yLjgtMi44YzAtLjgzMy4yNzItMS42MjkuNzY2LTIuMjQxYS41OTYuNTk2IDAgMCAwIC4xMDEtLjM1OS42NjcuNjY3IDAgMCAwLS42NjctLjY2Ni41OC41OCAwIDAgMC0uMzU4LjEwMkEzLjU4NCAzLjU4NCAwIDAgMSAyLjggMTAuOCAyLjgwMyAyLjgwMyAwIDAgMSAwIDhjMC00LjQxMSAzLjU4OS04IDgtOHM4IDMuNTg5IDggOHoiIGlkPSJvdXRsaW5lIi8+PHBhdGggY2xhc3M9Imljb24td2hpdGUiIGQ9Ik01LjQgNy45MzNhMi42NyAyLjY3IDAgMCAxIDIuNjY3IDIuNjY2YzAgLjYwNi0uMTkzIDEuMTc5LS41NDQgMS42MTRhMS41OTkgMS41OTkgMCAwIDAtLjMyMy45ODcuOC44IDAgMCAwIC44LjhjMy4zMDkgMCA2LTIuNjkxIDYtNnMtMi42OTEtNi02LTYtNiAyLjY5MS02IDZjMCAuNDQxLjM1OS44LjguOC4zNzggMCAuNzI5LS4xMTQuOTg2LS4zMjJBMi41NjggMi41NjggMCAwIDEgNS40IDcuOTMzeiIgaWQ9Imljb25GZyIvPjxnIGlkPSJpY29uQmciPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNOCAxNWMtLjk5MiAwLTEuOC0uODA4LTEuOC0xLjggMC0uNjA2LjE5My0xLjE3OS41NDQtMS42MTMuMjA4LS4yNTkuMzIzLS42MDkuMzIzLS45ODcgMC0uOTE5LS43NDgtMS42NjYtMS42NjctMS42NjYtLjM3NyAwLS43MjguMTE1LS45ODYuMzIzQTIuNTggMi41OCAwIDAgMSAyLjggOS44QzEuODA4IDkuOCAxIDguOTkyIDEgOGMwLTMuODYgMy4xNC03IDctNyAzLjg1OSAwIDcgMy4xNCA3IDcgMCAzLjg1OS0zLjE0MSA3LTcgN3pNNS40IDcuOTMzYTIuNjcgMi42NyAwIDAgMSAyLjY2NyAyLjY2NmMwIC42MDYtLjE5MyAxLjE3OS0uNTQ0IDEuNjE0YTEuNTk5IDEuNTk5IDAgMCAwLS4zMjMuOTg3LjguOCAwIDAgMCAuOC44YzMuMzA5IDAgNi0yLjY5MSA2LTZzLTIuNjkxLTYtNi02LTYgMi42OTEtNiA2YzAgLjQ0MS4zNTkuOC44LjguMzc4IDAgLjcyOS0uMTE0Ljk4Ni0uMzIyQTIuNTY4IDIuNTY4IDAgMCAxIDUuNCA3LjkzM3oiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tcHVycGxlIiBkPSJNNC41IDUuMzc1YS44NzUuODc1IDAgMSAwIDAgMS43NS44NzUuODc1IDAgMCAwIDAtMS43NXoiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1ibHVlIiBkPSJNNy4xMjUgMy42MjVhLjg3NS44NzUgMCAxIDAgMCAxLjc1Ljg3NS44NzUgMCAwIDAgMC0xLjc1eiIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWdyZWVuIiBkPSJNMTAuNjI1IDQuNWEuODc1Ljg3NSAwIDEgMCAwIDEuNzUuODc1Ljg3NSAwIDAgMCAwLTEuNzV6Ii8+PHBhdGggY2xhc3M9Imljb24tdnMteWVsbG93IiBkPSJNMTEuNSA4YS44NzUuODc1IDAgMSAwIDAgMS43NS44NzUuODc1IDAgMCAwIDAtMS43NXoiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1yZWQiIGQ9Ik05Ljc1IDEwLjYyNWEuODc1Ljg3NSAwIDEgMCAwIDEuNzUuODc1Ljg3NSAwIDAgMCAwLTEuNzV6Ii8+PC9nPjwvc3ZnPg=="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.file,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.file { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX08L3N0eWxlPjxwYXRoIGNsYXNzPSJpY29uLWNhbnZhcy10cmFuc3BhcmVudCIgZD0iTTE2IDE2SDBWMGgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNSAxNkgyVjBoOC42MjFMMTUgNC4zNzlWMTZ6IiBpZD0ib3V0bGluZSIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNMTMgMTRINFYyaDV2NGg0djh6bS0zLTlWMi4yMDdMMTIuNzkzIDVIMTB6IiBpZD0iaWNvbkZnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtYmciIGQ9Ik0zIDF2MTRoMTFWNC43OTNMMTAuMjA3IDFIM3ptMTAgMTNINFYyaDV2NGg0djh6bS0zLTlWMi4yMDdMMTIuNzkzIDVIMTB6IiBpZD0iaWNvbkJnIi8+PC9zdmc+"); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.reference,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.reference { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHN0eWxlPi5pY29uLWNhbnZhcy10cmFuc3BhcmVudHtvcGFjaXR5OjA7ZmlsbDojMmQyZDMwfS5pY29uLXZzLW91dHtmaWxsOiMyZDJkMzB9Lmljb24tdnMtYmd7ZmlsbDojYzVjNWM1fS5pY29uLXZzLWZne2ZpbGw6IzJiMjgyZX0uaWNvbi12cy1hY3Rpb24tYmx1ZXtmaWxsOiM3NWJlZmZ9PC9zdHlsZT48cGF0aCBjbGFzcz0iaWNvbi1jYW52YXMtdHJhbnNwYXJlbnQiIGQ9Ik0xNiAxNkgwVjBoMTZ2MTZ6IiBpZD0iY2FudmFzIi8+PHBhdGggY2xhc3M9Imljb24tdnMtb3V0IiBkPSJNMTQgNC41NTZWMTNjMCAuOTctLjcwMSAyLTIgMkg0Yy0uOTcgMC0yLS43MDEtMi0yVjYuNjQ5QTMuNDk1IDMuNDk1IDAgMCAxIDAgMy41QzAgMS41NyAxLjU3IDAgMy41IDBINXYxaDUuMDYxTDE0IDQuNTU2eiIgaWQ9Im91dGxpbmUiIHN0eWxlPSJkaXNwbGF5OiBub25lOyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWJnIiBkPSJNMTMgNXY4cy0uMDM1IDEtMS4wMzUgMWgtOFMzIDE0IDMgMTNWOWgxdjRoOFY2SDkuMzk3bC41MTctLjUyTDkgNC41NzJWM0g3LjQxOUw2LjQxMyAyaDMuMjI4TDEzIDV6IiBpZD0iaWNvbkJnIi8+PHBhdGggY2xhc3M9Imljb24tdnMtZmciIGQ9Ik03LjQxOSAzSDl2MS41NzJMNy40MTkgM3ptMS45NzggM0w2LjQxNiA5SDR2NGg4VjZIOS4zOTd6IiBpZD0iaWNvbkZnIiBzdHlsZT0iZGlzcGxheTogbm9uZTsiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1hY3Rpb24tYmx1ZSIgZD0iTTUuOTg4IDZIMy41YTIuNSAyLjUgMCAxIDEgMC01SDR2MWgtLjVDMi42NzMgMiAyIDIuNjczIDIgMy41UzIuNjczIDUgMy41IDVoMi41MTNMNCAzaDJsMi41IDIuNDg0TDYgOEg0bDEuOTg4LTJ6IiBpZD0iY29sb3JBY3Rpb24iLz48L3N2Zz4="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.snippet,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.snippet { background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0ic3ZnNDY5NCIKICAgdmlld0JveD0iMCAwIDE2IDE2Ij4KICA8bWV0YWRhdGEKICAgICBpZD0ibWV0YWRhdGE0NzA1Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZGVmcwogICAgIGlkPSJkZWZzNDcwMyIgLz4KICA8c3R5bGUKICAgICBpZD0ic3R5bGU0Njk2Ij4uaWNvbi1jYW52YXMtdHJhbnNwYXJlbnR7b3BhY2l0eTowO2ZpbGw6I2Y2ZjZmNn0uaWNvbi12cy1vdXR7ZmlsbDojZjZmNmY2fS5pY29uLXZzLWFjdGlvbi1vcmFuZ2V7ZmlsbDojYzI3ZDFhfTwvc3R5bGU+CiAgPGcKICAgICBpZD0iZzQ3MjQiCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMS4zMzMzMzMzLDAsMCwxLjMzMzMzMzMsLTI0NS45OTk5OSwtMzEuOTk5OTk5KSI+CiAgICA8cGF0aAogICAgICAgZD0ibSAxODUsMjQgMTEsMCAwLDEyIC0xMSwwIHoiCiAgICAgICBpZD0icGF0aDQ1MjgiCiAgICAgICBzdHlsZT0iZmlsbDojMmQyZDMwIiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gMTk0LDMzIDAsLTcgLTcsMCAwLDcgLTEsMCAwLC04IDksMCAwLDggeiBtIC04LDEgMSwwIDAsMSAtMSwwIHogbSAyLDAgMSwwIDAsMSAtMSwwIHogbSAyLDAgMSwwIDAsMSAtMSwwIHogbSAyLDAgMSwwIDAsMSAtMSwwIHogbSAyLDAgMSwwIDAsMSAtMSwwIHoiCiAgICAgICBpZD0icGF0aDQ1MzAiCiAgICAgICBzdHlsZT0iZmlsbDojYzVjNWM1IiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gMTg3LDI2IDcsMCAwLDcgLTcsMCB6IgogICAgICAgaWQ9InBhdGg0NTMyIgogICAgICAgc3R5bGU9ImZpbGw6IzJiMjgyZSIgLz4KICA8L2c+Cjwvc3ZnPgo="); }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.customcolor,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.customcolor { background-image: none; }

.monaco-editor.vs-dark .suggest-widget .monaco-list .monaco-list-row .icon.folder,
.monaco-editor.hc-black .suggest-widget .monaco-list .monaco-list-row .icon.folder { background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uaWNvbi1jYW52YXMtdHJhbnNwYXJlbnR7b3BhY2l0eTowO2ZpbGw6I0Y2RjZGNjt9IC5pY29uLXZzLW91dHtvcGFjaXR5OjA7ZmlsbDojRjZGNkY2O30gLmljb24tdnMtZmd7b3BhY2l0eTowO2ZpbGw6I0YwRUZGMTt9IC5pY29uLWZvbGRlcntmaWxsOiNDNUM1QzU7fTwvc3R5bGU+PHBhdGggY2xhc3M9Imljb24tY2FudmFzLXRyYW5zcGFyZW50IiBkPSJNMTYgMTZoLTE2di0xNmgxNnYxNnoiIGlkPSJjYW52YXMiLz48cGF0aCBjbGFzcz0iaWNvbi12cy1vdXQiIGQ9Ik0xNiAyLjV2MTBjMCAuODI3LS42NzMgMS41LTEuNSAxLjVoLTExLjk5NmMtLjgyNyAwLTEuNS0uNjczLTEuNS0xLjV2LThjMC0uODI3LjY3My0xLjUgMS41LTEuNWgyLjg4NmwxLTJoOC4xMWMuODI3IDAgMS41LjY3MyAxLjUgMS41eiIgaWQ9Im91dGxpbmUiLz48cGF0aCBjbGFzcz0iaWNvbi1mb2xkZXIiIGQ9Ik0xNC41IDJoLTcuNDkybC0xIDJoLTMuNTA0Yy0uMjc3IDAtLjUuMjI0LS41LjV2OGMwIC4yNzYuMjIzLjUuNS41aDExLjk5NmMuMjc1IDAgLjUtLjIyNC41LS41di0xMGMwLS4yNzYtLjIyNS0uNS0uNS0uNXptLS40OTYgMmgtNi40OTZsLjUtMWg1Ljk5NnYxeiIgaWQ9Imljb25CZyIvPjxwYXRoIGNsYXNzPSJpY29uLXZzLWZnIiBkPSJNMTQgM3YxaC02LjVsLjUtMWg2eiIgaWQ9Imljb25GZyIvPjwvc3ZnPg=="); }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .accessibilityHelpWidget {
	padding: 10px;
	vertical-align: middle;
	overflow: scroll;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .tokens-inspect-widget {
	z-index: 50;
	-webkit-user-select: text;
	-ms-user-select: text;
	-khtml-user-select: text;
	-moz-user-select: text;
	-o-user-select: text;
	user-select: text;
	padding: 10px;
}

.tokens-inspect-separator {
	height: 1px;
	border: 0;
}

.monaco-editor .tokens-inspect-widget .tm-token {
	font-family: monospace;
}

.monaco-editor .tokens-inspect-widget .tm-token-length {
	font-weight: normal;
	font-size: 60%;
	float: right;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-table {
	width: 100%;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-value {
	font-family: monospace;
	text-align: right;
}

.monaco-editor .tokens-inspect-widget .tm-token-type {
	font-family: monospace;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .iPadShowKeyboard {
	width: 58px;
	min-width: 0;
	height: 36px;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	resize: none;
	overflow: hidden;
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1OCIgaGVpZ2h0PSIzNiI+PHBhdGggZmlsbD0iI0YwRUZGMSIgZD0iTTU0IDMydi0yOGgtNTB2MjhoNTB6bS0xNi0yaC0xOHYtNmgxOHY2em02IDBoLTR2LTZoNHY2em04IDBoLTZ2LTZoNnY2em0tNC0yNGg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bS02LTEyaDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptLTYtMTJoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0tNi0xMmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bS02LTEyaDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptLTYtMTJoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDEyaC00di02aDR2NnptLTYtMjRoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0tNi0xMmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg2djZoLTZ2LTZ6Ii8+PHBhdGggZmlsbD0iIzQyNDI0MiIgZD0iTTU1LjMzNiAwaC01My4yODVjLTEuMzQ0IDAtMi4wNTEuNjU2LTIuMDUxIDJ2MzJjMCAxLjM0NC43MDcgMS45NjUgMi4wNTEgMS45NjVsNTMuOTQ5LjAzNWMxLjM0NCAwIDItLjY1NiAyLTJ2LTMyYzAtMS4zNDQtMS4zMi0yLTIuNjY0LTJ6bS0xLjMzNiAzMmgtNTB2LTI4aDUwdjI4eiIvPjxyZWN0IHg9IjYiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTIiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTgiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMjQiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzAiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzYiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNDIiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNDgiIHk9IjEyIiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNiIgeT0iNiIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjEyIiB5PSI2IiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTgiIHk9IjYiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIyNCIgeT0iNiIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjMwIiB5PSI2IiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzYiIHk9IjYiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0MiIgeT0iNiIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjQ4IiB5PSI2IiBmaWxsPSIjNDI0MjQyIiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNiIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIxMiIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIxOCIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIyNCIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIzMCIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIzNiIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0MiIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0OCIgeT0iMTgiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI2IiB5PSIyNCIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjYiIGhlaWdodD0iNiIvPjxyZWN0IHg9IjQ2IiB5PSIyNCIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjYiIGhlaWdodD0iNiIvPjxyZWN0IHg9IjIwIiB5PSIyNCIgZmlsbD0iIzQyNDI0MiIgd2lkdGg9IjE4IiBoZWlnaHQ9IjYiLz48cmVjdCB4PSIxNCIgeT0iMjQiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjYiLz48cmVjdCB4PSI0MCIgeT0iMjQiIGZpbGw9IiM0MjQyNDIiIHdpZHRoPSI0IiBoZWlnaHQ9IjYiLz48L3N2Zz4=") center center no-repeat;
	border: 4px solid #F6F6F6;
	border-radius: 4px;
}

.monaco-editor.vs-dark .iPadShowKeyboard {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1OCIgaGVpZ2h0PSIzNiI+PHBhdGggZmlsbD0iIzJCMjgyRSIgZD0iTTU0IDMydi0yOGgtNTB2MjhoNTB6bS0xNi0yaC0xOHYtNmgxOHY2em02IDBoLTR2LTZoNHY2em04IDBoLTZ2LTZoNnY2em0tNC0yNGg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bS02LTEyaDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptLTYtMTJoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0tNi0xMmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bS02LTEyaDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptMCA2aDR2NGgtNHYtNHptLTYtMTJoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDEyaC00di02aDR2NnptLTYtMjRoNHY0aC00di00em0wIDZoNHY0aC00di00em0wIDZoNHY0aC00di00em0tNi0xMmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg0djRoLTR2LTR6bTAgNmg2djZoLTZ2LTZ6Ii8+PHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTU1LjMzNiAwaC01My4yODVjLTEuMzQ0IDAtMi4wNTEuNjU2LTIuMDUxIDJ2MzJjMCAxLjM0NC43MDcgMS45NjUgMi4wNTEgMS45NjVsNTMuOTQ5LjAzNWMxLjM0NCAwIDItLjY1NiAyLTJ2LTMyYzAtMS4zNDQtMS4zMi0yLTIuNjY0LTJ6bS0xLjMzNiAzMmgtNTB2LTI4aDUwdjI4eiIvPjxyZWN0IHg9IjYiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTIiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTgiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMjQiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzAiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzYiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNDIiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNDgiIHk9IjEyIiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNiIgeT0iNiIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjEyIiB5PSI2IiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMTgiIHk9IjYiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIyNCIgeT0iNiIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjMwIiB5PSI2IiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iMzYiIHk9IjYiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0MiIgeT0iNiIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjQiIGhlaWdodD0iNCIvPjxyZWN0IHg9IjQ4IiB5PSI2IiBmaWxsPSIjQzVDNUM1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0Ii8+PHJlY3QgeD0iNiIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIxMiIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIxOCIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIyNCIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIzMCIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSIzNiIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0MiIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI0OCIgeT0iMTgiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjQiLz48cmVjdCB4PSI2IiB5PSIyNCIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjYiIGhlaWdodD0iNiIvPjxyZWN0IHg9IjQ2IiB5PSIyNCIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjYiIGhlaWdodD0iNiIvPjxyZWN0IHg9IjIwIiB5PSIyNCIgZmlsbD0iI0M1QzVDNSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjYiLz48cmVjdCB4PSIxNCIgeT0iMjQiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjYiLz48cmVjdCB4PSI0MCIgeT0iMjQiIGZpbGw9IiNDNUM1QzUiIHdpZHRoPSI0IiBoZWlnaHQ9IjYiLz48L3N2Zz4=") center center no-repeat;
	border: 4px solid #252526;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	font-size: 13px;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon,
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon {
	background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMDAiIGhlaWdodD0iNDAiPjxwYXRoIGQ9Ik0yODguNDgzIDMzYy0uNzcyIDAtMS40OTctLjEyMy0yLjE1My0uMzY1LS42NzgtLjI1My0xLjI3LS42MTctMS43Ni0xLjA4NC0uNS0uNDc1LS44OTItMS4wNDktMS4xNjMtMS43MDQtLjI3LS42NDQtLjQwNy0xLjM3MS0uNDA3LTIuMTU4IDAtLjUxNy4wNjEtMS4wMTguMTc4LTEuNDkuMTE2LS40Ny4yOS0uOTI1LjUxNi0xLjM0OC4yMjUtLjQyMi41MDgtLjgxNS44NDQtMS4xNjcuMzM0LS4zNTIuNzE3LS42NTYgMS4xMzktLjkwNS40MTYtLjI0Ni44ODEtLjQ0IDEuMzgtLjU3Ni40OTMtLjEzNCAxLjAyNi0uMjAyIDEuNTg3LS4yMDIuNzA1IDAgMS4zODIuMTA5IDIuMDEzLjMyNC42NDIuMjE3IDEuMjE4LjUzOCAxLjcwOC45NTUuNTAxLjQyNS45MDMuOTQ4IDEuMTkzIDEuNTU2LjI5NC42MjMuNDQyIDEuMzE2LjQ0MiAyLjA2NCAwIC42MTktLjA5IDEuMTg1LS4yNjggMS42NzktLjE3OC40OTItLjQyLjkyLS43MjEgMS4yNzUtLjMzMS4zNzctLjY5OS42NTgtMS4xMDQuODQ3bC0uMDQ4LjAyMnYxLjUzbC0uNTg3LjI2NmMtLjEyOC4wNTktLjI4OC4xMTctLjQ3NC4xNzktLjE5My4wNjItLjQwNC4xMTQtLjY0NS4xNTktLjIyOS4wNC0uNDc3LjA3Ni0uNzUzLjEwMy0uMjcuMDI3LS41NzguMDQtLjkxNy4wNHoiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNMjkxLjcxNiAyNC4wNDFjLS4zOTYtLjMzNi0uODU2LS41OTMtMS4zODQtLjc3MS0uNTI3LS4xOC0xLjA5LS4yNzEtMS42ODktLjI3MS0uNDczIDAtLjkxMi4wNTUtMS4zMjQuMTY3LS40MTQuMTEyLS43OTEuMjctMS4xMzUuNDczLS4zNDIuMjAyLS42NS40NDYtLjkyMi43MzMtLjI3My4yODYtLjUwMi42MDItLjY4Ni45NDktLjE4Ni4zNDctLjMzLjcyMi0uNDI4IDEuMTE5LS4xLjM5OS0uMTQ4LjgxNC0uMTQ4IDEuMjQ3IDAgLjY1Mi4xMDkgMS4yNDcuMzMyIDEuNzc2LjIxOS41MzEuNTMuOTg0LjkyOCAxLjM2MS4zOTYuMzc4Ljg3MS42NjcgMS40MTYuODcuNTQ4LjIwMiAxLjE1Mi4zMDQgMS44MDguMzA0LjMwMiAwIC41NzctLjAxMS44MjMtLjAzNS4yNDYtLjAyMy40NjgtLjA1Ni42NjQtLjA5MS4xOTUtLjAzNi4zNjYtLjA3OC41MTQtLjEyNWwuMzc1LS4xNHYtLjg1NGwtLjQ2My4xODRjLS4xNi4wNTYtLjMzNi4xMDQtLjUyMS4xNDMtLjE4OC4wMzctLjM4Ny4wNjktLjYwNC4wODktLjIxMy4wMjQtLjQ0OC4wMzQtLjcuMDM0LS41NjIgMC0xLjA2NC0uMDg4LTEuNTA5LS4yNjQtLjQ0Mi0uMTc2LS44MTYtLjQyMS0xLjEyNS0uNzMxLS4zMDktLjMxNC0uNTQ1LS42ODctLjcwOC0xLjEyNC0uMTYxLS40MzUtLjI0My0uOTEzLS4yNDMtMS40MzIgMC0uNTQ1LjA5LTEuMDUzLjI3My0xLjUyMi4xODItLjQ3MS40MzUtLjg3OS43NTgtMS4yMjUuMzI0LS4zNDUuNzA4LS42MTcgMS4xNTUtLjgxNS40NDYtLjE5Ni45MzQtLjI5NCAxLjQ1Ny0uMjk0LjQxOSAwIC43OTguMDQ0IDEuMTIyLjEzNi4zMjkuMDkxLjYyLjIxNS44NzEuMzY5LjI1NC4xNTguNDY1LjMzOS42NDMuNTQ3LjE3OS4yMDkuMzI0LjQzMi40MzguNjY3LjExMy4yMzcuMTkzLjQ4LjI0Ni43MzEuMDUxLjI1NC4wNzYuNS4wNzYuNzQxIDAgLjM0NC0uMDMzLjY1My0uMTAyLjkyNi0uMDY4LjI3NC0uMTU4LjUwMy0uMjY5LjY5NC0uMTEuMTg5LS4yMzkuMzM1LS4zODYuNDM0cy0uMjk1LjE0OC0uNDUzLjE0OGwtLjIxNS0uMDQ1Yy0uMDY2LS4wMjktLjExOS0uMDgtLjE2Ni0uMTU2LS4wNDYtLjA3NS0uMDgyLS4xNzctLjEwNy0uMzA2LS4wMjUtLjEyNi0uMDM5LS4yOTItLjAzOS0uNDkybC4wMTgtLjMyNS4wNDEtLjUzLjA1NS0uNjQ0LjA1OC0uNjQ3LjA0OC0uNTQ2LjAyNy0uMzQ0aC0uOTE5bC0uMDU0LjZoLS4wMjFjLS4wMjUtLjEwMy0uMDctLjE5NS0uMTM2LS4yODEtLjA2My0uMDgzLS4xNDEtLjE1NS0uMjMzLS4yMTYtLjA5MS0uMDYxLS4xOTMtLjEwNi0uMzA3LS4xNDEtLjExNS0uMDMzLS4yMzgtLjA0OC0uMzY5LS4wNDgtLjMzNyAwLS42NDYuMDctLjkyNC4yMTYtLjI4MS4xNDQtLjUxOC4zNDQtLjcyMS41OTktLjIwMS4yNTQtLjM1NS41NTYtLjQ2NS45MDUtLjExNS4zNS0uMTcuNzI2LS4xNyAxLjEzNCAwIC4zNDQuMDQ1LjY0NS4xMzUuOTAxLjA4OC4yNi4yMTEuNDczLjM1OS42NDYuMTUzLjE3MS4zMjkuMy41MzQuMzgyLjIuMDg2LjQxNS4xMjkuNjQxLjEyOS4xNzYgMCAuMzQyLS4wMjcuNDk5LS4wODEuMTU0LS4wNTIuMzAyLS4xMy40MzItLjIzMi4xMzQtLjEwNC4yNDgtLjIzLjM0OC0uMzguMTAyLS4xNDkuMTgyLS4zMjMuMjM2LS41MmguMDI3YzAgLjM3Ni4xMDEuNjc0LjMwNy44OTMuMjA3LjIyLjUwMi4zMy44ODkuMzMuMjkyIDAgLjU4LS4wNjQuODYzLS4xOTguMjgzLS4xMzIuNTM2LS4zMjguNzYyLS41ODYuMjIzLS4yNjIuNDA0LS41ODMuNTQzLS45NjYuMTM4LS4zODQuMjA4LS44My4yMDgtMS4zNCAwLS42MDUtLjExNy0xLjE1LS4zNDUtMS42MzQtLjIzMS0uNDgyLS41NDYtLjg5MS0uOTM5LTEuMjI1bS0yLjM2OCAzLjc3NGMtLjA1Ni4yNzctLjEzNi41MTctLjI0Ni43MTktLjEwOS4yMDMtLjI0Ni4zNjMtLjQwNy40ODEtLjE2My4xMTUtLjM1NC4xNzYtLjU3Mi4xNzYtLjEyIDAtLjIzNi0uMDI1LS4zNDQtLjA3OC0uMTA4LS4wNTItLjIwNi0uMTMtLjI4OS0uMjMyLS4wODEtLjEwMy0uMTQ4LS4yMzQtLjE5OC0uMzktLjA0Ni0uMTU2LS4wNy0uMzM3LS4wNy0uNTQ3IDAtLjIzNy4wMjctLjQ4MS4wOC0uNzI5LjA1Ni0uMjQ3LjEzNy0uNDczLjI1LS42NzcuMTA5LS4yLjI1LS4zNjMuNDE2LS40OTIuMTY1LS4xMjcuMzYxLS4xOTEuNTgyLS4xOTEuMTIzIDAgLjIzNC4wMjEuMzQuMDYzLjEwNy4wNDIuMTk4LjEwNy4yNzkuMTk2LjA4LjA4Ny4xNDUuMTk3LjE4OS4zMy4wNDMuMTM0LjA3LjI5NC4wNy40OCAwIC4zMTctLjAzMS42MTUtLjA4Ljg5MSIgZmlsbD0iI0M1QzVDNSIvPjxwYXRoIGQ9Ik0yODguNDgzIDEzYy0uNzcyIDAtMS40OTctLjEyMy0yLjE1My0uMzY1LS42NzgtLjI1My0xLjI3LS42MTctMS43Ni0xLjA4NC0uNS0uNDc1LS44OTItMS4wNDktMS4xNjMtMS43MDQtLjI2OS0uNjQ0LS40MDctMS4zNzEtLjQwNy0yLjE1OSAwLS41MTcuMDYxLTEuMDE4LjE3OC0xLjQ5LjExNi0uNDcuMjktLjkyNS41MTYtMS4zNDguMjI1LS40MjIuNTA4LS44MTUuODQ0LTEuMTY3LjMzNC0uMzUyLjcxNy0uNjU2IDEuMTM5LS45MDUuNDE2LS4yNDYuODgxLS40NCAxLjM4LS41NzYuNDkyLS4xMzQgMS4wMjUtLjIwMiAxLjU4Ni0uMjAyLjcwNSAwIDEuMzgyLjEwOSAyLjAxMy4zMjQuNjQyLjIxNyAxLjIxOC41MzggMS43MDguOTU1LjUwMS40MjUuOTAzLjk0OCAxLjE5MyAxLjU1Ni4yOTUuNjI0LjQ0MyAxLjMxNy40NDMgMi4wNjUgMCAuNjE5LS4wOSAxLjE4NS0uMjY4IDEuNjc5LS4xNzguNDkyLS40Mi45Mi0uNzIxIDEuMjc1LS4zMzEuMzc3LS42OTkuNjU4LTEuMTA0Ljg0N2wtLjA0OC4wMjJ2MS41M2wtLjU4Ny4yNjZjLS4xMjguMDU5LS4yODguMTE3LS40NzQuMTc5LS4xOTMuMDYyLS40MDQuMTE0LS42NDUuMTU5LS4yMjkuMDQtLjQ3Ny4wNzYtLjc1My4xMDMtLjI3LjAyNy0uNTc4LjA0LS45MTcuMDR6IiBmaWxsPSIjRjNGM0YzIi8+PHBhdGggZD0iTTI5MS43MTYgNC4wNDFjLS4zOTYtLjMzNi0uODU2LS41OTMtMS4zODQtLjc3MS0uNTI3LS4xNzktMS4wOS0uMjctMS42ODktLjI3LS40NzMgMC0uOTEyLjA1NS0xLjMyNC4xNjctLjQxNC4xMTItLjc5MS4yNy0xLjEzNS40NzMtLjM0Mi4yMDItLjY1LjQ0Ni0uOTIyLjczMy0uMjczLjI4Ni0uNTAyLjYwMi0uNjg2Ljk0OS0uMTg2LjM0Ny0uMzMuNzIyLS40MjggMS4xMTktLjA5OS40LS4xNDguODE1LS4xNDggMS4yNDcgMCAuNjUyLjEwOSAxLjI0Ny4zMzIgMS43NzYuMjE5LjUzMS41My45ODQuOTI4IDEuMzYxLjM5Ni4zNzguODcxLjY2NyAxLjQxNi44Ny41NDguMjAyIDEuMTUyLjMwNCAxLjgwOC4zMDQuMzAyIDAgLjU3Ny0uMDExLjgyMy0uMDM1LjI0Ni0uMDIzLjQ2OC0uMDU2LjY2NC0uMDkxLjE5NS0uMDM2LjM2Ni0uMDc4LjUxNC0uMTI1bC4zNzUtLjE0di0uODU0bC0uNDYzLjE4NGMtLjE2LjA1Ni0uMzM2LjEwNC0uNTIxLjE0My0uMTg4LjAzNy0uMzg3LjA2OS0uNjA0LjA4OS0uMjEzLjAyNC0uNDQ4LjAzNC0uNy4wMzQtLjU2MiAwLTEuMDY0LS4wODgtMS41MDktLjI2NC0uNDQyLS4xNzYtLjgxNi0uNDIxLTEuMTI1LS43MzEtLjMwOS0uMzE0LS41NDUtLjY4Ny0uNzA4LTEuMTI0LS4xNjEtLjQzNS0uMjQzLS45MTMtLjI0My0xLjQzMiAwLS41NDUuMDktMS4wNTMuMjczLTEuNTIyLjE4Mi0uNDcxLjQzNS0uODc5Ljc1OC0xLjIyNS4zMjQtLjM0NS43MDgtLjYxNyAxLjE1NS0uODE1LjQ0Ni0uMTk2LjkzNC0uMjk0IDEuNDU3LS4yOTQuNDE5IDAgLjc5OC4wNDQgMS4xMjIuMTM2LjMyOS4wOTEuNjIuMjE1Ljg3MS4zNjkuMjU0LjE1OC40NjUuMzM5LjY0My41NDcuMTc5LjIwOS4zMjQuNDMyLjQzOC42NjcuMTEzLjIzNy4xOTMuNDguMjQ2LjczMS4wNTEuMjU0LjA3Ni41LjA3Ni43NDEgMCAuMzQ0LS4wMzMuNjUzLS4xMDIuOTI2LS4wNjguMjc0LS4xNTguNTAzLS4yNjkuNjk0LS4xMS4xODktLjIzOS4zMzUtLjM4Ni40MzRzLS4yOTUuMTQ4LS40NTMuMTQ4bC0uMjE1LS4wNDVjLS4wNjYtLjAyOS0uMTE5LS4wOC0uMTY2LS4xNTYtLjA0Ni0uMDc1LS4wODItLjE3Ny0uMTA3LS4zMDYtLjAyNS0uMTI2LS4wMzktLjI5Mi0uMDM5LS40OTJsLjAxOC0uMzI1LjA0MS0uNTMuMDU1LS42NDQuMDU4LS42NDcuMDQ4LS41NDYuMDI3LS4zNDRoLS45MTlsLS4wNTQuNmgtLjAyMWMtLjAyNS0uMTAzLS4wNy0uMTk1LS4xMzYtLjI4MS0uMDYzLS4wODMtLjE0MS0uMTU1LS4yMzMtLjIxNi0uMDkxLS4wNjEtLjE5My0uMTA2LS4zMDctLjE0MS0uMTE1LS4wMzMtLjIzOC0uMDQ4LS4zNjktLjA0OC0uMzM3IDAtLjY0Ni4wNy0uOTI0LjIxNi0uMjgxLjE0NC0uNTE4LjM0NC0uNzIxLjU5OS0uMjAxLjI1NC0uMzU1LjU1Ni0uNDY1LjkwNS0uMTE1LjM1LS4xNy43MjYtLjE3IDEuMTM0IDAgLjM0NC4wNDUuNjQ1LjEzNS45MDEuMDg4LjI2LjIxMS40NzMuMzU5LjY0Ni4xNTMuMTcxLjMyOS4zLjUzNC4zODIuMi4wODYuNDE1LjEyOS42NDEuMTI5LjE3NiAwIC4zNDItLjAyNy40OTktLjA4MS4xNTQtLjA1Mi4zMDItLjEzLjQzMi0uMjMyLjEzNC0uMTA0LjI0OC0uMjMuMzQ4LS4zOC4xMDItLjE0OS4xODItLjMyMy4yMzYtLjUyaC4wMjdjMCAuMzc2LjEwMS42NzQuMzA3Ljg5My4yMDcuMjIuNTAyLjMzLjg4OS4zMy4yOTIgMCAuNTgtLjA2NC44NjMtLjE5OC4yODMtLjEzMi41MzYtLjMyOC43NjItLjU4Ni4yMjMtLjI2Mi40MDQtLjU4My41NDMtLjk2Ni4xMzgtLjM4NS4yMDgtLjgzMS4yMDgtMS4zNDEgMC0uNjA1LS4xMTctMS4xNS0uMzQ1LTEuNjM0LS4yMzEtLjQ4Mi0uNTQ2LS44OTEtLjkzOS0xLjIyNW0tMi4zNjggMy43NzRjLS4wNTYuMjc3LS4xMzYuNTE3LS4yNDYuNzE5LS4xMDkuMjAzLS4yNDYuMzYzLS40MDcuNDgxLS4xNjMuMTE1LS4zNTQuMTc2LS41NzIuMTc2LS4xMiAwLS4yMzYtLjAyNS0uMzQ0LS4wNzgtLjEwOC0uMDUyLS4yMDYtLjEzLS4yODktLjIzMi0uMDgxLS4xMDMtLjE0OC0uMjM0LS4xOTgtLjM5LS4wNDYtLjE1Ni0uMDctLjMzNy0uMDctLjU0NyAwLS4yMzcuMDI3LS40ODEuMDgtLjcyOS4wNTYtLjI0Ny4xMzctLjQ3My4yNS0uNjc3LjEwOS0uMi4yNS0uMzYzLjQxNi0uNDkyLjE2NS0uMTI3LjM2MS0uMTkxLjU4Mi0uMTkxLjEyMyAwIC4yMzQuMDIxLjM0LjA2My4xMDcuMDQyLjE5OC4xMDcuMjc5LjE5Ni4wOC4wODcuMTQ1LjE5Ny4xODkuMzMuMDQzLjEzNC4wNy4yOTQuMDcuNDggMCAuMzE3LS4wMzEuNjE1LS4wOC44OTEiIGZpbGw9IiM0MjQyNDIiLz48cGF0aCBkPSJNMjY0IDM3di0xNGg4LjYyNWwzLjM3NSAzLjU1NnYxMC40NDRoLTEyeiIgZmlsbD0iIzJEMkQyRCIvPjxwYXRoIGQ9Ik0yNzIgMjRoLTd2MTJoMTB2LTlsLTMtM3ptMiAxMWgtOHYtMTBoNXYzaDN2N3oiIGZpbGw9IiNDNUM1QzUiLz48cG9seWdvbiBwb2ludHM9IjI2NiwyNSAyNzEsMjUgMjcxLDI4IDI3NCwyOCAyNzQsMzUgMjY2LDM1IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTI2NCAxN3YtMTRoOC42MjVsMy4zNzUgMy41NTZ2MTAuNDQ0aC0xMnoiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNMjcyIDRoLTd2MTJoMTB2LTlsLTMtM3ptMiAxMWgtOHYtMTBoNXYzaDN2N3oiIGZpbGw9IiM0MjQyNDIiLz48cG9seWdvbiBwb2ludHM9IjI2Niw1IDI3MSw1IDI3MSw4IDI3NCw4IDI3NCwxNSAyNjYsMTUiIGZpbGw9IiNGMEVGRjEiLz48cG9seWdvbiBwb2ludHM9IjI0NywzNCAyNDcsMzAgMjQ1LDMwIDI0NSwyNiAyNTUsMjYgMjU1LDM0IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTI1NCAyOWgtOHYtMmg4djJ6bTAgMWgtNnYxaDZ2LTF6bTAgMmgtNnYxaDZ2LTF6IiBmaWxsPSIjQzVDNUM1Ii8+PHBvbHlnb24gcG9pbnRzPSIyNDcsMTQgMjQ3LDEwIDI0NSwxMCAyNDUsNiAyNTUsNiAyNTUsMTQiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNMjU0IDloLTh2LTJoOHYyem0wIDFoLTZ2MWg2di0xem0wIDJoLTZ2MWg2di0xeiIgZmlsbD0iIzQyNDI0MiIvPjxwYXRoIGQ9Ik0yMzAuNSAyMmMtNC4xNDMgMC03LjUgMy4zNTctNy41IDcuNXMzLjM1NyA3LjUgNy41IDcuNSA3LjUtMy4zNTcgNy41LTcuNS0zLjM1Ny03LjUtNy41LTcuNXptMCAxMWMtMS45MzMgMC0zLjUtMS41NjYtMy41LTMuNXMxLjU2Ny0zLjUgMy41LTMuNSAzLjUgMS41NjYgMy41IDMuNS0xLjU2NyAzLjUtMy41IDMuNXoiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNMjI0LjAyNSAyOWMuMTA4LTEuNDE4LjY2OS0yLjcwOCAxLjU0Mi0zLjcyNmwxLjQzMSAxLjQzMWMtLjUxNi42NDYtLjg1MSAxLjQzLS45NDcgMi4yOTVoLTIuMDI2em0yLjk3MyAzLjI5NWMtLjUxNi0uNjQ2LS44NTEtMS40My0uOTQ3LTIuMjk1aC0yLjAyNWMuMTA4IDEuNDE4LjY2OSAyLjcwNyAxLjU0MiAzLjcyNmwxLjQzLTEuNDMxem00LjAwMi05LjI3djIuMDI1Yy44NjUuMDk3IDEuNjQ5LjQzMiAyLjI5NS45NDdsMS40MzEtMS40MzFjLTEuMDE4LS44NzItMi4zMDgtMS40MzItMy43MjYtMS41NDF6bS0zLjI5NSAyLjk3M2MuNjQ2LS41MTYgMS40My0uODUxIDIuMjk1LS45NDd2LTIuMDI1Yy0xLjQxOC4xMDgtMi43MDguNjY5LTMuNzI2IDEuNTQybDEuNDMxIDEuNDN6bTYuMjk3LjcwN2MuNTE2LjY0Ni44NTEgMS40My45NDcgMi4yOTVoMi4wMjVjLS4xMDgtMS40MTgtLjY2OS0yLjcwOC0xLjU0Mi0zLjcyNmwtMS40MyAxLjQzMXptLTQuMDAyIDcuMjQ0Yy0uODY1LS4wOTctMS42NDktLjQzMi0yLjI5NS0uOTQ3bC0xLjQzMSAxLjQzMWMxLjAxOC44NzMgMi4zMDcgMS40MzQgMy43MjYgMS41NDJ2LTIuMDI2em00Ljk0OS0zLjk0OWMtLjA5Ny44NjUtLjQzMiAxLjY0OC0uOTQ3IDIuMjk1bDEuNDMxIDEuNDMxYy44NzMtMS4wMTkgMS40MzQtMi4zMDggMS41NDItMy43MjZoLTIuMDI2em0tMS42NTQgMy4wMDJjLS42NDYuNTE2LTEuNDMuODUxLTIuMjk1Ljk0N3YyLjAyNWMxLjQxOS0uMTA4IDIuNzA4LS42NjkgMy43MjYtMS41NDJsLTEuNDMxLTEuNDN6IiBmaWxsPSIjQzVDNUM1Ii8+PHBhdGggZD0iTTIzMC41IDJjLTQuMTQzIDAtNy41IDMuMzU4LTcuNSA3LjUgMCA0LjE0MyAzLjM1NyA3LjUgNy41IDcuNXM3LjUtMy4zNTcgNy41LTcuNWMwLTQuMTQyLTMuMzU3LTcuNS03LjUtNy41em0wIDExYy0xLjkzMyAwLTMuNS0xLjU2Ni0zLjUtMy41IDAtMS45MzMgMS41NjctMy41IDMuNS0zLjVzMy41IDEuNTY3IDMuNSAzLjVjMCAxLjkzNC0xLjU2NyAzLjUtMy41IDMuNXoiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNMjI0LjAyNSA5Yy4xMDgtMS40MTguNjY5LTIuNzA4IDEuNTQyLTMuNzI2bDEuNDMxIDEuNDMxYy0uNTE2LjY0Ni0uODUxIDEuNDMtLjk0NyAyLjI5NGgtMi4wMjZ6bTIuOTczIDMuMjk1Yy0uNTE2LS42NDYtLjg1MS0xLjQzLS45NDctMi4yOTVoLTIuMDI1Yy4xMDggMS40MTguNjY5IDIuNzA3IDEuNTQyIDMuNzI2bDEuNDMtMS40MzF6bTQuMDAyLTkuMjd2Mi4wMjVjLjg2NS4wOTcgMS42NDkuNDMyIDIuMjk1Ljk0OGwxLjQzMS0xLjQzMWMtMS4wMTgtLjg3My0yLjMwOC0xLjQzMy0zLjcyNi0xLjU0MnptLTMuMjk1IDIuOTc0Yy42NDYtLjUxNiAxLjQzLS44NTEgMi4yOTUtLjk0OHYtMi4wMjZjLTEuNDE4LjEwOC0yLjcwOC42NjktMy43MjYgMS41NDJsMS40MzEgMS40MzJ6bTYuMjk3LjcwN2MuNTE2LjY0Ni44NTEgMS40My45NDcgMi4yOTRoMi4wMjVjLS4xMDgtMS40MTgtLjY2OS0yLjcwOC0xLjU0Mi0zLjcyNmwtMS40MyAxLjQzMnptLTQuMDAyIDcuMjQzYy0uODY1LS4wOTctMS42NDktLjQzMi0yLjI5NS0uOTQ3bC0xLjQzMSAxLjQzMWMxLjAxOC44NzMgMi4zMDcgMS40MzQgMy43MjYgMS41NDJ2LTIuMDI2em00Ljk0OS0zLjk0OWMtLjA5Ny44NjUtLjQzMiAxLjY0OC0uOTQ3IDIuMjk1bDEuNDMxIDEuNDMxYy44NzMtMS4wMTkgMS40MzQtMi4zMDggMS41NDItMy43MjZoLTIuMDI2em0tMS42NTQgMy4wMDJjLS42NDYuNTE2LTEuNDMuODUxLTIuMjk1Ljk0N3YyLjAyNWMxLjQxOS0uMTA4IDIuNzA4LS42NjkgMy43MjYtMS41NDJsLTEuNDMxLTEuNDN6IiBmaWxsPSIjNDI0MjQyIi8+PHJlY3QgeD0iMjAyIiB5PSIyMyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE0IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTIwMyAyNHYxMmgxNHYtMTJoLTE0em0xMyAxMWgtMTJ2LTEwaDEydjEwem0tNi03di0xaC0xdjVoM3YtNGgtMnptMSAzaC0xdi0yaDF2MnptMy0ydjJoMXYxaC0ydi00aDJ2MWgtMXptLTYtMXY0aC0zdi0yaDF2MWgxdi0xaC0xdi0xaC0xdi0xaDN6IiBmaWxsPSIjQzVDNUM1Ii8+PHBhdGggZD0iTTIxMCAyOWgxdjJoLTF2LTJ6bS0zIDJ2LTFoLTF2MWgxem05LTZ2MTBoLTEydi0xMGgxMnptLTggM2gtM3YxaDF2MWgtMXYyaDN2LTR6bTQgMGgtMnYtMWgtMXY1aDN2LTR6bTMgMGgtMnY0aDJ2LTFoLTF2LTJoMXYtMXoiIGZpbGw9IiMyRDJEMkQiLz48cmVjdCB4PSIyMDIiIHk9IjMiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNCIgZmlsbD0iI0YzRjNGMyIvPjxwYXRoIGQ9Ik0yMDMgNHYxMmgxNHYtMTJoLTE0em0xMyAxMWgtMTJ2LTEwaDEydjEwem0tNi03di0xaC0xdjVoM3YtNGgtMnptMSAzaC0xdi0yaDF2MnptMy0ydjJoMXYxaC0ydi00aDJ2MWgtMXptLTYtMXY0aC0zdi0yaDF2MWgxdi0xaC0xdi0xaC0xdi0xaDN6IiBmaWxsPSIjNDI0MjQyIi8+PHBhdGggZD0iTTIxMCA5aDF2MmgtMXYtMnptLTMgMnYtMWgtMXYxaDF6bTktNnYxMGgtMTJ2LTEwaDEyem0tOCAzaC0zdjFoMXYxaC0xdjJoM3YtNHptNCAwaC0ydi0xaC0xdjVoM3YtNHptMyAwaC0ydjRoMnYtMWgtMXYtMmgxdi0xeiIgZmlsbD0iI0YwRUZGMSIvPjxwYXRoIGQ9Ik0xOTYuNjUyIDMyLjVjLjgxMS0uNTM3IDEuMzQ4LTEuNDU3IDEuMzQ4LTIuNSAwLTEuNjU0LTEuMzQ2LTMtMy0zLS43NzEgMC0xLjQ2OC4zMDEtMiAuNzc5di01Ljc3OWgtMTF2MTJoMy43NjRsLTEuNDUyLjcyNyAxLjQ4MSAxLjQ4Yy4zMjIuMzIyLjgwMy41IDEuMzU0LjUuNDM2IDAgLjg5Ny0uMTExIDEuMzAxLS4zMTNsMy4xNDQtMS41NzJjLjEzNC4wNTMuMjcxLjA5OC40MTQuMTI3bC0uMDA1LjA1MWMwIDEuNjU0IDEuMzQ2IDMgMyAzczMtMS4zNDYgMy0zYy0uMDAxLTEuMDQzLS41MzgtMS45NjMtMS4zNDktMi41eiIgZmlsbD0iIzJEMkQyRCIvPjxwYXRoIGQ9Ik0xOTUgMzNjLS4yOTMgMC0uNTY5LjA2Ni0uODIuMThsLS4yNS0uMjVjLjA0Mi0uMTM3LjA3LS4yNzkuMDctLjQzcy0uMDI4LS4yOTMtLjA3LS40M2wuMjUtLjI1Yy4yNTEuMTEzLjUyNy4xOC44Mi4xOCAxLjEwNCAwIDItLjg5NiAyLTIgMC0xLjEwNS0uODk2LTItMi0ycy0yIC44OTUtMiAyYzAgLjI5My4wNjYuNTY4LjE4LjgybC0uMjUuMjVjLS4xMzctLjA0My0uMjc5LS4wNy0uNDMtLjA3LS4zMzcgMC0uNjQ1LjExNS0uODk1LjMwM2wtMi42MDctMS4zMDUtLjk5OS0uNWMtLjU1Mi0uMjc1LTEuMjIzLS4yNzUtMS40OTkuMDAybC0uNS41IDUgMi41LTUgMi41LjUuNWMuMjc2LjI3NS45NDcuMjc1IDEuNSAwbDEtLjUgMi42MDUtMS4zMDNjLjI1LjE4OC41NTguMzAzLjg5NS4zMDMuMTUgMCAuMjkzLS4wMjkuNDMtLjA3bC4yNS4yNWMtLjExNC4yNS0uMTguNTI3LS4xOC44MiAwIDEuMTA0Ljg5NiAyIDIgMnMyLS44OTYgMi0yYzAtMS4xMDUtLjg5Ni0yLTItMnptMC00Yy41NTMgMCAxIC40NDcgMSAxIDAgLjU1MS0uNDQ3IDEtMSAxcy0xLS40NDktMS0xYzAtLjU1My40NDctMSAxLTF6bS0yLjUgNGMtLjI3NiAwLS41LS4yMjUtLjUtLjUgMC0uMjc3LjIyNC0uNS41LS41cy41LjIyMy41LjVjMCAuMjc1LS4yMjQuNS0uNS41em0yLjUgM2MtLjU1MyAwLTEtLjQ0OS0xLTEgMC0uNTUzLjQ0Ny0xIDEtMXMxIC40NDcgMSAxYzAgLjU1MS0uNDQ3IDEtMSAxem0tMy0xM3Y3LjA1MWMtLjE0Mi4wMjktLjI3OS4wNy0uNDEzLjEyM2wtLjU4Ny0uMTc0di02aC03djdoLTF2LThoOXptLTggMTBoLTF2LTFoMXYxem0yLTFoLTF2MWgxdi0xem0yIDBoLTF2MWgxdi0xeiIgZmlsbD0iI0M1QzVDNSIvPjxwYXRoIGQ9Ik0xODUuNzkzIDI4Ljc5M2wtMS43OTMgMS4yMDd2LTZoN3Y1LjM4MWwtMi41NTQtLjc3N2MtLjgxNi0uNDA5LTEuOTktLjQ3NS0yLjY1My4xODl6bS0uNzkzIDIuMjA3aC43NjRsLS43NjQtLjM4M3YuMzgzem0xMSA0YzAgLjU1MS0uNDQ3IDEtMSAxcy0xLS40NDktMS0xYzAtLjU1My40NDctMSAxLTFzMSAuNDQ3IDEgMXptLTMuNS0zYy0uMjc2IDAtLjUuMjIzLS41LjUgMCAuMjc1LjIyNC41LjUuNXMuNS0uMjI1LjUtLjVjMC0uMjc3LS4yMjQtLjUtLjUtLjV6bTIuNS0zYy0uNTUzIDAtMSAuNDQ3LTEgMSAwIC41NTEuNDQ3IDEgMSAxczEtLjQ0OSAxLTFjMC0uNTUzLS40NDctMS0xLTF6IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTE5Ni42NTIgMTIuNWMuODExLS41MzggMS4zNDgtMS40NTggMS4zNDgtMi41IDAtMS42NTQtMS4zNDYtMy0zLTMtLjc3MSAwLTEuNDY4LjMwMS0yIC43Nzl2LTUuNzc5aC0xMXYxMmgzLjc2NGwtMS40NTIuNzI3IDEuNDgxIDEuNDhjLjMyMi4zMjIuODAzLjUgMS4zNTQuNS40MzYgMCAuODk3LS4xMTEgMS4zMDEtLjMxM2wzLjE0NC0xLjU3MmMuMTM0LjA1My4yNzEuMDk4LjQxNC4xMjdsLS4wMDUuMDUxYzAgMS42NTQgMS4zNDYgMyAzIDNzMy0xLjM0NiAzLTNjLS4wMDEtMS4wNDMtLjUzOC0xLjk2My0xLjM0OS0yLjV6IiBmaWxsPSIjRjNGM0YzIi8+PHBhdGggZD0iTTE5NSAxM2MtLjI5MyAwLS41NjkuMDY2LS44Mi4xOGwtLjI1LS4yNWMuMDQyLS4xMzcuMDctLjI3OS4wNy0uNDNzLS4wMjgtLjI5My0uMDctLjQzbC4yNS0uMjVjLjI1MS4xMTMuNTI3LjE4LjgyLjE4IDEuMTA0IDAgMi0uODk2IDItMiAwLTEuMTA1LS44OTYtMi0yLTJzLTIgLjg5NS0yIDJjMCAuMjkzLjA2Ni41NjguMTguODJsLS4yNS4yNWMtLjEzNy0uMDQzLS4yNzktLjA3LS40My0uMDctLjMzNyAwLS42NDUuMTE1LS44OTUuMzAzbC0yLjYwNy0xLjMwNC0uOTk5LS41Yy0uNTUyLS4yNzUtMS4yMjMtLjI3NS0xLjQ5OS4wMDJsLS41LjQ5OSA1IDIuNS01IDIuNS41LjVjLjI3Ni4yNzUuOTQ3LjI3NSAxLjUgMGwxLS41IDIuNjA1LTEuMzAzYy4yNS4xODguNTU4LjMwMy44OTUuMzAzLjE1IDAgLjI5My0uMDI5LjQzLS4wN2wuMjUuMjVjLS4xMTMuMjUtLjE4LjUyNy0uMTguODIgMCAxLjEwNC44OTYgMiAyIDJzMi0uODk2IDItMmMwLTEuMTA2LS44OTYtMi0yLTJ6bTAtNGMuNTUzIDAgMSAuNDQ3IDEgMSAwIC41NTEtLjQ0NyAxLTEgMXMtMS0uNDQ5LTEtMWMwLS41NTMuNDQ3LTEgMS0xem0tMi41IDRjLS4yNzYgMC0uNS0uMjI1LS41LS41IDAtLjI3Ny4yMjQtLjUuNS0uNXMuNS4yMjMuNS41YzAgLjI3NS0uMjI0LjUtLjUuNXptMi41IDNjLS41NTMgMC0xLS40NDktMS0xIDAtLjU1My40NDctMSAxLTFzMSAuNDQ3IDEgMWMwIC41NS0uNDQ3IDEtMSAxem0tMy0xM3Y3LjA1MWMtLjE0Mi4wMjktLjI3OS4wNy0uNDEzLjEyM2wtLjU4Ny0uMTc0di02aC03djdoLTF2LThoOXptLTggMTBoLTF2LTFoMXYxem0yLTFoLTF2MWgxdi0xem0yIDBoLTF2MWgxdi0xeiIgZmlsbD0iIzQyNDI0MiIvPjxwYXRoIGQ9Ik0xODUuNzkzIDguNzkzbC0xLjc5MyAxLjIwN3YtNmg3djUuMzgxbC0yLjU1NC0uNzc3Yy0uODE2LS40MDktMS45OS0uNDc1LTIuNjUzLjE4OXptLS43OTMgMi4yMDdoLjc2NGwtLjc2NC0uMzgzdi4zODN6bTExIDRjMCAuNTUxLS40NDcgMS0xIDFzLTEtLjQ0OS0xLTFjMC0uNTUzLjQ0Ny0xIDEtMXMxIC40NDcgMSAxem0tMy41LTNjLS4yNzYgMC0uNS4yMjMtLjUuNSAwIC4yNzUuMjI0LjUuNS41cy41LS4yMjUuNS0uNWMwLS4yNzgtLjIyNC0uNS0uNS0uNXptMi41LTNjLS41NTMgMC0xIC40NDctMSAxIDAgLjU1MS40NDcgMSAxIDFzMS0uNDQ5IDEtMWMwLS41NTMtLjQ0Ny0xLTEtMXoiIGZpbGw9IiNGMEVGRjEiLz48cGF0aCBkPSJNMTc4IDI3di0zaC03di0xaC05djE0aDEzdi0zaDN2LTNoLTF2LTNoLTZ2LTFoN3ptLTggN3YtM2gxdjNoLTF6IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTE3NyAyNmgtNXYtMWg1djF6bS0xIDNoLTJ2MWgydi0xem0tNCAwaC05djFoOXYtMXptMiA2aC0xMXYxaDExdi0xem0tNS0zaC02djFoNnYtMXptOCAwaC01djFoNXYtMXptLTctOHYzaC03di0zaDd6bS0xIDFoLTV2MWg1di0xeiIgZmlsbD0iI0M1QzVDNSIvPjxyZWN0IHg9IjE2NCIgeT0iMjUiIHdpZHRoPSI1IiBoZWlnaHQ9IjEiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNMTc4IDd2LTNoLTd2LTFoLTl2MTRoMTN2LTNoM3YtM2gtMXYtM2gtNnYtMWg3em0tOCA3di0zaDF2M2gtMXoiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNMTc3IDZoLTV2LTFoNXYxem0tMSAzaC0ydjFoMnYtMXptLTQgMGgtOXYxaDl2LTF6bTIgNmgtMTF2MWgxMXYtMXptLTUtM2gtNnYxaDZ2LTF6bTggMGgtNXYxaDV2LTF6bS03LTh2M2gtN3YtM2g3em0tMSAxaC01djFoNXYtMXoiIGZpbGw9IiM0MjQyNDIiLz48cmVjdCB4PSIxNjQiIHk9IjUiIHdpZHRoPSI1IiBoZWlnaHQ9IjEiIGZpbGw9IiNGMEVGRjEiLz48cG9seWdvbiBwb2ludHM9IjE1NC40MTQsMjQgMTQ5LjU4NiwyNCAxNDgsMjUuNTg2IDE0OCwyOCAxNDQsMjggMTQ0LDM1IDE1MiwzNSAxNTIsMzEgMTU0LjQxNCwzMSAxNTYsMjkuNDE0IDE1NiwyNS41ODYiIGZpbGw9IiMyRDJEMkQiLz48ZyBmaWxsPSIjNzVCRUZGIj48cGF0aCBkPSJNMTU0IDI1aC00bC0xIDF2Mmg1djFoLTJ2MWgybDEtMXYtM2wtMS0xem0wIDJoLTR2LTFoNHYxek0xNDUgMzRoNnYtNWgtNnY1em0xLTNoNHYxaC00di0xeiIvPjwvZz48ZyBmaWxsPSIjMkQyRDJEIj48cmVjdCB4PSIxNDYiIHk9IjMxIiB3aWR0aD0iNCIgaGVpZ2h0PSIxIi8+PHJlY3QgeD0iMTUwIiB5PSIyNiIgd2lkdGg9IjQiIGhlaWdodD0iMSIvPjxyZWN0IHg9IjE1MiIgeT0iMjgiIHdpZHRoPSIyIiBoZWlnaHQ9IjEiLz48L2c+PHBvbHlnb24gcG9pbnRzPSIxNTQuNDE0LDQgMTQ5LjU4Niw0IDE0OCw1LjU4NiAxNDgsOCAxNDQsOCAxNDQsMTUgMTUyLDE1IDE1MiwxMSAxNTQuNDE0LDExIDE1Niw5LjQxNCAxNTYsNS41ODYiIGZpbGw9IiNGM0YzRjMiLz48ZyBmaWxsPSIjMDA1MzlDIj48cGF0aCBkPSJNMTU0IDVoLTRsLTEgMXYyaDV2MWgtMnYxaDJsMS0xdi0zbC0xLTF6bTAgMmgtNHYtMWg0djF6TTE0NSAxNGg2di01aC02djV6bTEtM2g0djFoLTR2LTF6Ii8+PC9nPjxnIGZpbGw9IiNGMEVGRjEiPjxyZWN0IHg9IjE0NiIgeT0iMTEiIHdpZHRoPSI0IiBoZWlnaHQ9IjEiLz48cmVjdCB4PSIxNTAiIHk9IjYiIHdpZHRoPSI0IiBoZWlnaHQ9IjEiLz48cmVjdCB4PSIxNTIiIHk9IjgiIHdpZHRoPSIyIiBoZWlnaHQ9IjEiLz48L2c+PHBhdGggZD0iTTEzOCAyNGgtMTV2NGgtMXY4aDh2LTZoOHYtNnptLTExIDloLTJ2LTJoMnYyeiIgZmlsbD0iIzJEMkQyRCIvPjxwYXRoIGQ9Ik0xMzcgMjloLTd2LTFoLTZ2LTNoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXY0em0tMTIgMXYtMWgtMnY2aDJ2LTFoLTF2LTRoMXptMiA0djFoMnYtNmgtMnYxaDF2NGgtMXoiIGZpbGw9IiNDNUM1QzUiLz48cGF0aCBkPSJNMTI1IDI3di0yaDF2MmgtMXptMyAwdi0yaC0xdjJoMXptMiAwdi0yaC0xdjJoMXptMiAwdi0yaC0xdjJoMXptMiAwdi0yaC0xdjJoMXptMiAwdi0yaC0xdjJoMXoiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNMTM4IDRoLTE1djRoLTF2OGg4di02aDh2LTZ6bS0xMSA5aC0ydi0yaDJ2MnoiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNMTM3IDloLTd2LTFoLTZ2LTNoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXYyaDF2LTJoMXY0em0tMTIgMXYtMWgtMnY2aDJ2LTFoLTF2LTRoMXptMiA0djFoMnYtNmgtMnYxaDF2NGgtMXoiIGZpbGw9IiM0MjQyNDIiLz48cGF0aCBkPSJNMTI1IDd2LTJoMXYyaC0xem0zIDB2LTJoLTF2Mmgxem0yIDB2LTJoLTF2Mmgxem0yIDB2LTJoLTF2Mmgxem0yIDB2LTJoLTF2Mmgxem0yIDB2LTJoLTF2MmgxeiIgZmlsbD0iI0YwRUZGMSIvPjxwYXRoIGQ9Ik0xMTAuNDQ5IDIzYy0xLjYzNyAwLTMuMDc1Ljc5Ny0zLjk4NyAyLjAxMmwuMDAxLjAwMmMtLjYyOC44MzYtMS4wMTQgMS44NjMtMS4wMTQgMi45ODYgMCAuNDY5LjA2Ny45MzMuMiAxLjM4NWwtMi45MDcgMi45MDhjLS42ODcuNjg2LTEuMjUzIDIuMTYxIDAgMy40MTQuNjA5LjYwOSAxLjI0NC43MzYgMS42Ny43MzYuOTU4IDAgMS42MjEtLjYxMyAxLjc0NC0uNzM2bDIuOTA3LTIuOTA4Yy40NTMuMTMzLjkxNy4yMDEgMS4zODYuMjAxIDEuMTIzIDAgMi4xNDktLjM4NyAyLjk4NS0xLjAxNGwuMDAyLjAwMWMxLjIxNi0uOTEyIDIuMDEzLTIuMzUyIDIuMDEzLTMuOTg3IDAtMi43NjItMi4yMzgtNS01LTV6IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTExNC4wOSAyNi4zNTlsLTIuNjQxIDIuNjQxLTItMiAyLjY0MS0yLjY0MWMtLjUwMi0uMjI3LTEuMDU1LS4zNTktMS42NDEtLjM1OS0yLjIwOSAwLTQgMS43OTEtNCA0IDAgLjU4Ni4xMzMgMS4xMzkuMzU5IDEuNjRsLTMuMzU5IDMuMzZzLTEgMSAwIDJoMmwzLjM1OS0zLjM2Yy41MDIuMjI3IDEuMDU1LjM2IDEuNjQxLjM2IDIuMjA5IDAgNC0xLjc5MSA0LTQgMC0uNTg2LS4xMzMtMS4xMzktLjM1OS0xLjY0MXoiIGZpbGw9IiNDNUM1QzUiLz48cGF0aCBkPSJNMTEwLjQ0OSAzYy0xLjYzNyAwLTMuMDc1Ljc5Ny0zLjk4NyAyLjAxMmwuMDAxLjAwMmMtLjYyOC44MzYtMS4wMTQgMS44NjMtMS4wMTQgMi45ODYgMCAuNDY5LjA2Ny45MzMuMiAxLjM4NWwtMi45MDcgMi45MDhjLS42ODcuNjg2LTEuMjUzIDIuMTYxIDAgMy40MTQuNjA5LjYwOSAxLjI0NC43MzYgMS42Ny43MzYuOTU4IDAgMS42MjEtLjYxMyAxLjc0NC0uNzM2bDIuOTA3LTIuOTA4Yy40NTMuMTMzLjkxNy4yMDEgMS4zODYuMjAxIDEuMTIzIDAgMi4xNDktLjM4NyAyLjk4NS0xLjAxNGwuMDAyLjAwMWMxLjIxNi0uOTEyIDIuMDEzLTIuMzUyIDIuMDEzLTMuOTg3IDAtMi43NjItMi4yMzgtNS01LTV6IiBmaWxsPSIjRjNGM0YzIi8+PHBhdGggZD0iTTExNC4wOSA2LjM1OWwtMi42NDEgMi42NDEtMi0yIDIuNjQxLTIuNjQxYy0uNTAyLS4yMjYtMS4wNTUtLjM1OS0xLjY0MS0uMzU5LTIuMjA5IDAtNCAxLjc5MS00IDQgMCAuNTg2LjEzMyAxLjEzOS4zNTkgMS42NGwtMy4zNTkgMy4zNnMtMSAxIDAgMmgybDMuMzU5LTMuMzZjLjUwMi4yMjcgMS4wNTUuMzYgMS42NDEuMzYgMi4yMDkgMCA0LTEuNzkxIDQtNCAwLS41ODYtLjEzMy0xLjEzOS0uMzU5LTEuNjQxeiIgZmlsbD0iIzQyNDI0MiIvPjxwYXRoIGQ9Ik04OSAzM2gxdi0xYzAtLjUzNy43NDEtMS42MTMgMS0yLS4yNTktLjM4OS0xLTEuNDY3LTEtMnYtMWgtMXYtM2gxYzEuOTY5LjAyMSAzIDEuMjc3IDMgM3YxbDEgMXYybC0xIDF2MWMwIDEuNzA5LTEuMDMxIDIuOTc5LTMgM2gtMXYtM3ptLTIgMGgtMXYtMWMwLS41MzctLjc0MS0xLjYxMy0xLTIgLjI1OS0uMzg5IDEtMS40NjcgMS0ydi0xaDF2LTNoLTFjLTEuOTY5LjAyMS0zIDEuMjc3LTMgM3YxbC0xIDF2MmwxIDF2MWMwIDEuNzA5IDEuMzE3IDIuOTc5IDMuMjg2IDNoLjcxNHYtM3oiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNOTEgMzN2LTFjMC0uODM0LjQ5Ni0xLjczOCAxLTItLjUwNC0uMjctMS0xLjE2OC0xLTJ2LTFjMC0uODQtLjU4NC0xLTEtMXYtMWMyLjA4MyAwIDIgMS4xNjYgMiAydjFjMCAuOTY5LjcwMy45OCAxIDF2MmMtLjMyMi4wMi0xIC4wNTMtMSAxdjFjMCAuODM0LjA4MyAyLTIgMnYtMWMuODMzIDAgMS0xIDEtMXptLTYgMHYtMWMwLS44MzQtLjQ5Ni0xLjczOC0xLTIgLjUwNC0uMjcgMS0xLjE2OCAxLTJ2LTFjMC0uODQuNTg0LTEgMS0xdi0xYy0yLjA4MyAwLTIgMS4xNjYtMiAydjFjMCAuOTY5LS43MDMuOTgtMSAxdjJjLjMyMi4wMiAxIC4wNTMgMSAxdjFjMCAuODM0LS4wODMgMiAyIDJ2LTFjLS44MzMgMC0xLTEtMS0xeiIgZmlsbD0iI0M1QzVDNSIvPjxwYXRoIGQ9Ik04OSAxM2gxdi0xYzAtLjUzNy43NDEtMS42MTMgMS0yLS4yNTktLjM4OS0xLTEuNDY3LTEtMnYtMWgtMXYtM2gxYzEuOTY5LjAyMSAzIDEuMjc3IDMgM3YxbDEgMXYybC0xIDF2MWMwIDEuNzA5LTEuMDMxIDIuOTc5LTMgM2gtMXYtM3ptLTIgMGgtMXYtMWMwLS41MzctLjc0MS0xLjYxMy0xLTIgLjI1OS0uMzg5IDEtMS40NjcgMS0ydi0xaDF2LTNoLTFjLTEuOTY5LjAyMS0zIDEuMjc3LTMgM3YxbC0xIDF2MmwxIDF2MWMwIDEuNzA5IDEuMzE3IDIuOTc5IDMuMjg2IDNoLjcxNHYtM3oiIGZpbGw9IiNGM0YzRjMiLz48cGF0aCBkPSJNOTEgMTN2LTFjMC0uODM0LjQ5Ni0xLjczOCAxLTItLjUwNC0uMjctMS0xLjE2OC0xLTJ2LTFjMC0uODQtLjU4NC0xLTEtMXYtMWMyLjA4MyAwIDIgMS4xNjYgMiAydjFjMCAuOTY5LjcwMy45OCAxIDF2MmMtLjMyMi4wMi0xIC4wNTMtMSAxdjFjMCAuODM0LjA4MyAyLTIgMnYtMWMuODMzIDAgMS0xIDEtMXptLTYgMHYtMWMwLS44MzQtLjQ5Ni0xLjczOC0xLTIgLjUwNC0uMjcgMS0xLjE2OCAxLTJ2LTFjMC0uODQuNTg0LTEgMS0xdi0xYy0yLjA4MyAwLTIgMS4xNjYtMiAydjFjMCAuOTY5LS43MDMuOTgtMSAxdjJjLjMyMi4wMiAxIC4wNTMgMSAxdjFjMCAuODM0LS4wODMgMiAyIDJ2LTFjLS44MzMgMC0xLTEtMS0xeiIgZmlsbD0iIzQyNDI0MiIvPjxwYXRoIGQ9Ik03My41IDM0Yy0xLjkxNCAwLTMuNjAxLTEuMjQyLTQuMjI3LTNoLTEuNjgzYy0uNTI0LjkxLTEuNTAzIDEuNS0yLjU5MSAxLjUtMS42NTQgMC0zLTEuMzQ2LTMtM3MxLjM0Ni0zIDMtM2MxLjA4OCAwIDIuMDY2LjU4OCAyLjU5MSAxLjVoMS42ODNjLjYyNi0xLjc2IDIuMzEzLTMgNC4yMjctMyAyLjQ4MSAwIDQuNSAyLjAxOCA0LjUgNC41IDAgMi40OC0yLjAxOSA0LjUtNC41IDQuNXoiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNNzMuNSAyNmMtMS43NTkgMC0zLjIwNCAxLjMwOC0zLjQ0OSAzaC0zLjEyMmMtLjIyMy0uODYxLS45OTgtMS41LTEuOTI5LTEuNS0xLjEwNCAwLTIgLjg5NS0yIDIgMCAxLjEwNC44OTYgMiAyIDIgLjkzMSAwIDEuNzA2LS42MzkgMS45MjktMS41aDMuMTIyYy4yNDUgMS42OTEgMS42OSAzIDMuNDQ5IDMgMS45MyAwIDMuNS0xLjU3IDMuNS0zLjUgMC0xLjkzMS0xLjU3LTMuNS0zLjUtMy41em0wIDVjLS44MjcgMC0xLjUtLjY3NC0xLjUtMS41IDAtLjgyOC42NzMtMS41IDEuNS0xLjVzMS41LjY3MiAxLjUgMS41YzAgLjgyNi0uNjczIDEuNS0xLjUgMS41eiIgZmlsbD0iIzc1QkVGRiIvPjxjaXJjbGUgY3g9IjczLjUiIGN5PSIyOS41IiByPSIxLjUiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNNzMuNSAxNGMtMS45MTQgMC0zLjYwMS0xLjI0Mi00LjIyNy0zaC0xLjY4M2MtLjUyNC45MS0xLjUwMyAxLjUtMi41OTEgMS41LTEuNjU0IDAtMy0xLjM0Ni0zLTNzMS4zNDYtMyAzLTNjMS4wODggMCAyLjA2Ni41ODggMi41OTEgMS41aDEuNjgzYy42MjYtMS43NiAyLjMxMy0zIDQuMjI3LTMgMi40ODEgMCA0LjUgMi4wMTggNC41IDQuNSAwIDIuNDgtMi4wMTkgNC41LTQuNSA0LjV6IiBmaWxsPSIjRjNGM0YzIi8+PHBhdGggZD0iTTczLjUgNmMtMS43NTkgMC0zLjIwNCAxLjMwOC0zLjQ0OSAzaC0zLjEyMmMtLjIyMy0uODYxLS45OTgtMS41LTEuOTI5LTEuNS0xLjEwNCAwLTIgLjg5NS0yIDIgMCAxLjEwNC44OTYgMiAyIDIgLjkzMSAwIDEuNzA2LS42MzkgMS45MjktMS41aDMuMTIyYy4yNDUgMS42OTEgMS42OSAzIDMuNDQ5IDMgMS45MyAwIDMuNS0xLjU3IDMuNS0zLjUgMC0xLjkzMS0xLjU3LTMuNS0zLjUtMy41em0wIDVjLS44MjcgMC0xLjUtLjY3NC0xLjUtMS41IDAtLjgyOC42NzMtMS41IDEuNS0xLjVzMS41LjY3MiAxLjUgMS41YzAgLjgyNi0uNjczIDEuNS0xLjUgMS41eiIgZmlsbD0iIzAwNTM5QyIvPjxjaXJjbGUgY3g9IjczLjUiIGN5PSI5LjUiIHI9IjEuNSIgZmlsbD0iI0YwRUZGMSIvPjxwYXRoIGQ9Ik01OCAyOC41ODZsLTMtMy0xLjQxNCAxLjQxNGgtMi4xNzJsMS0xLTQtNGgtLjgyOGwtNS41ODYgNS41ODZ2LjgyOGw0IDQgMi40MTQtMi40MTRoLjU4NnY1aDEuNTg2bDMgM2guODI4bDMuNTg2LTMuNTg2di0uODI4bC0yLjA4Ni0yLjA4NiAyLjA4Ni0yLjA4NnYtLjgyOHoiIGZpbGw9IiMyRDJEMkQiLz48cG9seWdvbiBwb2ludHM9IjUzLjk5OCwzMy4wMDIgNTEsMzMgNTEsMjkgNTMsMjkgNTIsMzAgNTQsMzIgNTcsMjkgNTUsMjcgNTQsMjggNDksMjggNTEsMjYgNDgsMjMgNDMsMjggNDYsMzEgNDgsMjkgNTAsMjkgNTAsMzQgNTMsMzQgNTIsMzUgNTQsMzcgNTcsMzQgNTUsMzIiIGZpbGw9IiNDMjdEMUEiLz48cGF0aCBkPSJNNTggOC41ODZsLTMtMy0xLjQxNCAxLjQxNGgtMi4xNzJsMS0xLTQtNGgtLjgyOGwtNS41ODYgNS41ODZ2LjgyOGw0IDQgMi40MTQtMi40MTRoLjU4NnY1aDEuNTg2bDMgM2guODI4bDMuNTg2LTMuNTg2di0uODI4bC0yLjA4Ni0yLjA4NiAyLjA4Ni0yLjA4NnYtLjgyOHoiIGZpbGw9IiNGM0YzRjMiLz48cG9seWdvbiBwb2ludHM9IjUzLjk5OCwxMy4wMDIgNTEsMTMgNTEsOSA1Myw5IDUyLDEwIDU0LDEyIDU3LDkgNTUsNyA1NCw4IDQ5LDggNTEsNiA0OCwzIDQzLDggNDYsMTEgNDgsOSA1MCw5IDUwLDE0IDUzLDE0IDUyLDE1IDU0LDE3IDU3LDE0IDU1LDEyIiBmaWxsPSIjQzI3RDFBIi8+PHBhdGggZD0iTTI5LjI2MyAyNGw0LjczNyAyLjM2OXY1LjIzNmwtNi43OTEgMy4zOTVoLS40MmwtNC43ODktMi4zOTV2LTUuMjM2bDYuNzM5LTMuMzY5aC41MjR6IiBmaWxsPSIjMkQyRDJEIi8+PHBhdGggZD0iTTIzIDI4djRsNCAyIDYtM3YtNGwtNC0yLTYgM3ptNCAxbC0yLTEgNC0yIDIgMS00IDJ6IiBmaWxsPSIjNzVCRUZGIi8+PHBhdGggZD0iTTI5IDI2bDIgMS00IDItMi0xIDQtMnoiIGZpbGw9IiMyRDJEMkQiLz48cGF0aCBkPSJNMjkuMjYzIDRsNC43MzcgMi4zNjl2NS4yMzZsLTYuNzkxIDMuMzk1aC0uNDJsLTQuNzg5LTIuMzk1di01LjIzNmw2LjczOS0zLjM2OWguNTI0eiIgZmlsbD0iI0YzRjNGMyIvPjxwYXRoIGQ9Ik0yMyA4djRsNCAyIDYtM3YtNGwtNC0yLTYgM3ptNCAxbC0yLTEgNC0yIDIgMS00IDJ6IiBmaWxsPSIjMDA1MzlDIi8+PHBhdGggZD0iTTI5IDZsMiAxLTQgMi0yLTEgNC0yeiIgZmlsbD0iI0YwRUZGMSIvPjxwb2x5Z29uIHBvaW50cz0iMiwyNy4zMDggMiwzMi42OTIgNy4yMDksMzYgNy43OTEsMzYgMTMsMzIuNjkyIDEzLDI3LjMwOCA3Ljc5MSwyNCA3LjIwOSwyNCIgZmlsbD0iIzJEMkQyRCIvPjxwYXRoIGQ9Ik03LjUgMjVsLTQuNSAyLjg1N3Y0LjI4NWw0LjUgMi44NTggNC41LTIuODU3di00LjI4NWwtNC41LTIuODU4em0tLjUgOC40OThsLTMtMS45MDV2LTIuODE1bDMgMS45MDV2Mi44MTV6bS0yLjM1OC01LjQ5OGwyLjg1OC0xLjgxNSAyLjg1OCAxLjgxNS0yLjg1OCAxLjgxNS0yLjg1OC0xLjgxNXptNi4zNTggMy41OTNsLTMgMS45MDV2LTIuODE1bDMtMS45MDV2Mi44MTV6IiBmaWxsPSIjQjE4MEQ3Ii8+PHBvbHlnb24gcG9pbnRzPSIxMC4zNTgsMjggNy41LDI5LjgxNSA0LjY0MiwyOCA3LjUsMjYuMTg1IiBmaWxsPSIjMkQyRDJEIi8+PHBvbHlnb24gcG9pbnRzPSI0LDI4Ljc3NyA3LDMwLjY4MyA3LDMzLjQ5OCA0LDMxLjU5MyIgZmlsbD0iIzJEMkQyRCIvPjxwb2x5Z29uIHBvaW50cz0iOCwzMy40OTggOCwzMC42ODMgMTEsMjguNzc3IDExLDMxLjU5MyIgZmlsbD0iIzJEMkQyRCIvPjxwb2x5Z29uIHBvaW50cz0iMiw3LjMwOCAyLDEyLjY5MiA3LjIwOSwxNiA3Ljc5MSwxNiAxMywxMi42OTIgMTMsNy4zMDggNy43OTEsNCA3LjIwOSw0IiBmaWxsPSIjRjNGM0YzIi8+PHBhdGggZD0iTTcuNSA1bC00LjUgMi44NTd2NC4yODVsNC41IDIuODU4IDQuNS0yLjg1N3YtNC4yODZsLTQuNS0yLjg1N3ptLS41IDguNDk4bC0zLTEuOTA1di0yLjgxNmwzIDEuOTA1djIuODE2em0tMi4zNTgtNS40OThsMi44NTgtMS44MTUgMi44NTggMS44MTUtMi44NTggMS44MTUtMi44NTgtMS44MTV6bTYuMzU4IDMuNTkzbC0zIDEuOTA1di0yLjgxNWwzLTEuOTA1djIuODE1eiIgZmlsbD0iIzY1MkQ5MCIvPjxwb2x5Z29uIHBvaW50cz0iMTAuMzU4LDggNy41LDkuODE1IDQuNjQyLDggNy41LDYuMTg1IiBmaWxsPSIjRjBFRkYxIi8+PHBvbHlnb24gcG9pbnRzPSI0LDguNzc3IDcsMTAuNjgzIDcsMTMuNDk4IDQsMTEuNTkzIiBmaWxsPSIjRjBFRkYxIi8+PHBvbHlnb24gcG9pbnRzPSI4LDEzLjQ5OCA4LDEwLjY4MyAxMSw4Ljc3NyAxMSwxMS41OTMiIGZpbGw9IiNGMEVGRjEiLz48L3N2Zz4=");
	background-repeat: no-repeat;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.method,
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.function,
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.constructor		{ background-position: 0 -4px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.field,
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.variable 			{ background-position: -22px -4px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.class 				{ background-position: -43px -3px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.interface 			{ background-position: -63px -4px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.module 			{ background-position: -82px -4px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.property 			{ background-position: -102px -3px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.enum		 		{ background-position: -122px -3px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.rule		 		{ background-position: -242px -4px; }
.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.file		 		{ background-position: -262px -4px; }

.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.method,
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.function,
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.constructor 	{ background-position: 0 -24px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.field,
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.variable 		{ background-position: -22px -24px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.class 		{ background-position: -43px -23px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.interface 	{ background-position: -63px -24px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.module 		{ background-position: -82px -24px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.property 		{ background-position: -102px -23px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.enum		 	{ background-position: -122px -23px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.rule		 	{ background-position: -242px -24px; }
.vs-dark .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.file		 	{ background-position: -262px -24px; }

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon {
	background: none;
	display: inline;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon:before {
	height: 16px;
	width: 16px;
	display: inline-block;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.method:before,
.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.function:before,
.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.constructor:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI0IxODBENyIgZD0iTTUuNSAzbC00LjUgMi44NTd2NC4yODVsNC41IDIuODU4IDQuNS0yLjg1N3YtNC4yODZsLTQuNS0yLjg1N3ptLS41IDguNDk4bC0zLTEuOTA1di0yLjgxNmwzIDEuOTA1djIuODE2em0tMi4zNTgtNS40OThsMi44NTgtMS44MTUgMi44NTggMS44MTUtMi44NTggMS44MTUtMi44NTgtMS44MTV6bTYuMzU4IDMuNTkzbC0zIDEuOTA1di0yLjgxNWwzLTEuOTA1djIuODE1eiIvPjwvc3ZnPg==);
	margin-left: 2px;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.field:before,
.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.variable:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iIzc1QkVGRiIgZD0iTTEgNnY0bDQgMiA2LTN2LTRsLTQtMi02IDN6bTQgMWwtMi0xIDQtMiAyIDEtNCAyeiIvPjwvc3ZnPg==);
	margin-left: 2px;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.class:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBvbHlnb24gZmlsbD0iI0U4QUI1MyIgcG9pbnRzPSIxMS45OTgsMTEuMDAyIDksMTEgOSw3IDExLDcgMTAsOCAxMiwxMCAxNSw3IDEzLDUgMTIsNiA3LDYgOSw0IDYsMSAxLDYgNCw5IDYsNyA4LDcgOCwxMiAxMSwxMiAxMCwxMyAxMiwxNSAxNSwxMiAxMywxMCIvPjwvc3ZnPg==);
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.interface:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iIzc1QkVGRiIgZD0iTTExLjUgNGMtMS43NTkgMC0zLjIwNCAxLjMwOC0zLjQ0OSAzaC0zLjEyMmMtLjIyMy0uODYxLS45OTgtMS41LTEuOTI5LTEuNS0xLjEwNCAwLTIgLjg5NS0yIDIgMCAxLjEwNC44OTYgMiAyIDIgLjkzMSAwIDEuNzA2LS42MzkgMS45MjktMS41aDMuMTIyYy4yNDUgMS42OTEgMS42OSAzIDMuNDQ5IDMgMS45MyAwIDMuNS0xLjU3IDMuNS0zLjUgMC0xLjkzMS0xLjU3LTMuNS0zLjUtMy41em0wIDVjLS44MjcgMC0xLjUtLjY3NC0xLjUtMS41IDAtLjgyOC42NzMtMS41IDEuNS0xLjVzMS41LjY3MiAxLjUgMS41YzAgLjgyNi0uNjczIDEuNS0xLjUgMS41eiIvPjwvc3ZnPg==);
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.module:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTkgMTF2LTFjMC0uODM0LjQ5Ni0xLjczOCAxLTItLjUwNC0uMjctMS0xLjE2OC0xLTJ2LTFjMC0uODQtLjU4NC0xLTEtMXYtMWMyLjA4MyAwIDIgMS4xNjYgMiAydjFjMCAuOTY5LjcwMy45OCAxIDF2MmMtLjMyMi4wMi0xIC4wNTMtMSAxdjFjMCAuODM0LjA4MyAyLTIgMnYtMWMuODMzIDAgMS0xIDEtMXptLTYgMHYtMWMwLS44MzQtLjQ5Ni0xLjczOC0xLTIgLjUwNC0uMjcgMS0xLjE2OCAxLTJ2LTFjMC0uODQuNTg0LTEgMS0xdi0xYy0yLjA4MyAwLTIgMS4xNjYtMiAydjFjMCAuOTY5LS43MDMuOTgtMSAxdjJjLjMyMi4wMiAxIC4wNTMgMSAxdjFjMCAuODM0LS4wODMgMiAyIDJ2LTFjLS44MzMgMC0xLTEtMS0xeiIvPjwvc3ZnPg==);
	margin-left: 2px;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.property:before	{
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTEyLjA5IDQuMzU5bC0yLjY0MSAyLjY0MS0yLTIgMi42NDEtMi42NDFjLS41MDItLjIyNi0xLjA1NS0uMzU5LTEuNjQxLS4zNTktMi4yMDkgMC00IDEuNzkxLTQgNCAwIC41ODYuMTMzIDEuMTM5LjM1OSAxLjY0bC0zLjM1OSAzLjM2cy0xIDEgMCAyaDJsMy4zNTktMy4zNmMuNTAzLjIyNiAxLjA1NS4zNiAxLjY0MS4zNiAyLjIwOSAwIDQtMS43OTEgNC00IDAtLjU4Ni0uMTMzLTEuMTM5LS4zNTktMS42NDF6Ii8+PC9zdmc+);
	margin-left: 1px;
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.value:before,
.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.enum:before	{
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PGcgZmlsbD0iIzc1QkVGRiI+PHBhdGggZD0iTTEyIDNoLTRsLTEgMXYyaDV2MWgtMnYxaDJsMS0xdi0zbC0xLTF6bTAgMmgtNHYtMWg0djF6TTMgMTJoNnYtNWgtNnY1em0xLTNoNHYxaC00di0xeiIvPjwvZz48L3N2Zz4=);
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.rule:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTEwIDVoLTh2LTJoOHYyem0wIDFoLTZ2MWg2di0xem0wIDJoLTZ2MWg2di0xeiIvPjwvc3ZnPg==);
}

.hc-black .monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon.file:before {
	content: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZmlsbD0iI0M1QzVDNSIgZD0iTTkuNjc2IDJoLTYuNjc2djEyaDEwdi05bC0zLjMyNC0zem0yLjMyNCAxMWgtOHYtMTBoNXYzaDN2N3oiLz48L3N2Zz4=);
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	border-radius: 3px;
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	background-color: rgba(221, 221, 221, 0.4);
	vertical-align: middle;
	color: #555;
	font-size: 11px;
	padding: 3px 5px;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key,
.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	color: #ccc;
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 2px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	position: absolute;
	width: 600px;
	z-index: 2000;
	padding-bottom: 6px;
	left: 50%;
	margin-left: -300px;
}

.monaco-quick-open-widget .monaco-progress-container {
	position: absolute;
	left: 0;
	top: 38px;
	z-index: 1;
	height: 2px;
}

.monaco-quick-open-widget .monaco-progress-container .progress-bit {
	height: 2px;
}

.monaco-quick-open-widget .quick-open-input {
	width: 588px;
	border: none;
	margin: 6px;
}

.monaco-quick-open-widget .quick-open-input .monaco-inputbox {
	width: 100%;
	height: 25px;
}

.monaco-quick-open-widget .quick-open-tree {
	line-height: 22px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-tree-row  > .content > .sub-content {
	overflow: hidden;
}

.monaco-quick-open-widget.content-changing .quick-open-tree .monaco-scrollable-element .slider {
	display: none; /* scrollbar slider causes some hectic updates when input changes quickly, so hide it while quick open changes */
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry > .quick-open-row {
	display: flex;
	align-items: center;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon {
	overflow: hidden;
	width: 16px;
	height: 16px;
	margin-right: 4px;
	display: inline-block;
	vertical-align: middle;
	flex-shrink: 0;
}

.monaco-quick-open-widget .quick-open-tree .monaco-icon-label,
.monaco-quick-open-widget .quick-open-tree .monaco-icon-label .monaco-icon-label-description-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .monaco-highlighted-label span {
	opacity: 1;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry-meta {
	opacity: 0.7;
	line-height: normal;
}

.monaco-quick-open-widget .quick-open-tree .content.has-group-label .quick-open-entry-keybinding {
	margin-right: 8px;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry-keybinding .monaco-keybinding-key {
	vertical-align: text-bottom;
}

.monaco-quick-open-widget .quick-open-tree .results-group {
	margin-right: 18px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-tree-row.focused > .content.has-actions > .results-group,
.monaco-quick-open-widget .quick-open-tree .monaco-tree-row:hover:not(.highlighted) > .content.has-actions > .results-group,
.monaco-quick-open-widget .quick-open-tree .focused .monaco-tree-row.focused > .content.has-actions > .results-group {
	margin-right: 0px;
}

.monaco-quick-open-widget .quick-open-tree .results-group-separator {
	border-top-width: 1px;
	border-top-style: solid;
	box-sizing: border-box;
	margin-left: -11px;
	padding-left: 11px;
}

/* Actions in Quick Open Items */

.monaco-tree .monaco-tree-row > .content.actions {
	position: relative;
	display: flex;
}

.monaco-tree .monaco-tree-row > .content.actions > .sub-content {
	flex: 1;
}

.monaco-tree .monaco-tree-row > .content.actions .action-item {
	margin: 0;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar {
	line-height: 22px;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar {
	display: none;
	padding: 0 0.8em 0 0.4em;
}

.monaco-tree .monaco-tree-row.focused > .content.has-actions > .primary-action-bar {
	width: 0; /* in order to support a11y with keyboard, we use width: 0 to hide the actions, which still allows to "Tab" into the actions */
	display: block;
}

.monaco-tree .monaco-tree-row:hover:not(.highlighted) > .content.has-actions > .primary-action-bar,
.monaco-tree.focused .monaco-tree-row.focused > .content.has-actions > .primary-action-bar,
.monaco-tree .monaco-tree-row > .content.has-actions.more > .primary-action-bar {
	width: inherit;
	display: block;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar .action-label {
	margin-right: 0.4em;
	margin-top: 4px;
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-highlighted-label .highlight {
	font-weight: bold;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
	-webkit-transition: width 100ms linear;
	-o-transition: width 100ms linear;
	-moz-transition: width 100ms linear;
	-ms-transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	-ms-animation-name: progress;
	-ms-animation-duration: 4s;
	-ms-animation-iteration-count: infinite;
	-ms-animation-timing-function: linear;
	-webkit-animation-name: progress;
	-webkit-animation-duration: 4s;
	-webkit-animation-iteration-count: infinite;
	-webkit-animation-timing-function: linear;
	-moz-animation-name: progress;
	-moz-animation-duration: 4s;
	-moz-animation-iteration-count: infinite;
	-moz-animation-timing-function: linear;
	will-change: transform;
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 *  50%: 50 * 50 = 2500%
 * 100%: 50 * 100 - 50 (do not overflow): 4950%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }
@-ms-keyframes progress { from { transform: translateX(0%) scaleX(1) }	50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }
@-webkit-keyframes progress { from { transform: translateX(0%) scaleX(1) }	50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }
@-moz-keyframes progress { from { transform: translateX(0%) scaleX(1) }	50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	font-size: 13px;
}</style><style type="text/css" media="screen" class="monaco-colors">.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #000000; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.vs-whitespace { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .line-numbers { color: #2b91af; }
.monaco-editor .view-overlays .current-line { background-color: #f5f5f5; }
.monaco-editor .margin-view-overlays .current-line-margin { background-color: #f5f5f5; border: none; }
.monaco-editor .lines-content .cigr { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .lines-content .cigra { box-shadow: 1px 0 0 0 #939393 inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #add6ff; }
.monaco-editor .selected-text { background-color: #e5ebf1; }
.monaco-editor .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .minimap-slider, .monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover, .monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active, .monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23d60a0a'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23117711'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23008000'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-diff-editor .diff-review-line-number { color: #2b91af; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #b9b9b9; }
.monaco-editor .codelens-decoration { color: #999999; }
.monaco-editor .codelens-decoration > a:hover { color: #0000ff !important; }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #efeff2; }
.monaco-editor .find-widget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; width: 3px !important; margin-left: -4px;}
.monaco-editor .findOptionsWidget { background-color: #efeff2; }
.monaco-editor .findOptionsWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .reference-zone-widget .ref-tree .referenceMatch { background-color: rgba(234, 92, 0, 0.3); }
.monaco-editor .reference-zone-widget .preview .reference-decoration { background-color: rgba(245, 216, 2, 0.87); }
.monaco-editor .reference-zone-widget .ref-tree { background-color: #f3f3f3; }
.monaco-editor .reference-zone-widget .ref-tree { color: #646465; }
.monaco-editor .reference-zone-widget .ref-tree .reference-file { color: #1e1e1e; }
.monaco-editor .reference-zone-widget .ref-tree .monaco-tree.focused .monaco-tree-rows > .monaco-tree-row.selected:not(.highlighted) { background-color: rgba(51, 153, 255, 0.2); }
.monaco-editor .reference-zone-widget .ref-tree .monaco-tree.focused .monaco-tree-rows > .monaco-tree-row.selected:not(.highlighted) { color: #6c6c6c !important; }
.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {	background-color: #f2f8fc;}
.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {	background-color: #f2f8fc;}
.monaco-editor .monaco-editor-overlaymessage .anchor { border-top-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { border: 1px solid #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { background-color: #d6ecf2; }
.monaco-editor .goto-definition-link { color: #0000ff !important; }
.monaco-editor .hoverHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .monaco-editor-hover { background-color: #efeff2; }
.monaco-editor .monaco-editor-hover { border: 1px solid #c8c8c8; }
.monaco-editor .monaco-editor-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover a { color: #4080d0; }
.monaco-editor .monaco-editor-hover code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #b9b9b9; }
.monaco-editor .detected-link-active { color: #0000ff !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #c8c8c8; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #efeff2; }
.monaco-editor .parameter-hints-widget a { color: #4080d0; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight { color: #007acc; }
.monaco-editor .suggest-widget { color: #000000; }
.monaco-editor .suggest-widget a { color: #4080d0; }
.monaco-editor .suggest-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .focused .selectionHighlight { background-color: rgba(173, 214, 255, 0.3); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.25); }
.monaco-editor .wordHighlightStrong { background-color: rgba(14, 99, 156, 0.25); }
.monaco-editor .accessibilityHelpWidget { background-color: #efeff2; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .tokens-inspect-widget { border: 1px solid #c8c8c8; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #c8c8c8; }
.monaco-editor .tokens-inspect-widget { background-color: #efeff2; }

.mtk1 { color: #000000; }
.mtk2 { color: #fffffe; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #984e9c; }
.mtk6 { color: #0451a5; }
.mtk7 { color: #0000ff; }
.mtk8 { color: #ac9037; }
.mtk9 { color: #09885a; }
.mtk10 { color: #008000; }
.mtk11 { color: #aaaaaa; }
.mtk12 { color: #dd0000; }
.mtk13 { color: #383838; }
.mtk14 { color: #1f217d; }
.mtk15 { color: #cd3131; }
.mtk16 { color: #863b00; }
.mtk17 { color: #af00db; }
.mtk18 { color: #800000; }
.mtk19 { color: #e00000; }
.mtk20 { color: #3953a4; }
.mtk21 { color: #3030c0; }
.mtk22 { color: #666666; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #a31515; }
.mtk26 { color: #4f76ac; }
.mtk27 { color: #4d7fe2; }
.mtk28 { color: #008080; }
.mtk29 { color: #001188; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; }</style><style type="text/css" media="screen"></style><script type="text/javascript" charset="utf-8" async="" src="./hello_files/0.12f69cc02e5f71a8a143.bundle.js.download"></script><script type="text/javascript" charset="utf-8" async="" src="./hello_files/monaco_languageclient_813e49388618322cc224f3472d47cecb-d83f75c9665209aa2b7e.js.download"></script><style>.grecaptcha-badge:hover { left: 4px !important }</style><style>.grecaptcha-badge:hover { left: 4px !important }</style><link rel="alternate" type="application/json+oembed" href="https://repl.it/data/oembed?url=https%3A%2F%2Frepl.it%2F%40MateoMugen%2FSoggyKnobbyProducts" title="repl.it - select language" class="next-head"><style>.grecaptcha-badge:hover { left: 4px !important }</style><meta property="og:image" content="https://www.gravatar.com/avatar/a54d14695f564b6539b8ae1bc7fbb2e8?d=https://repl.it/public/images/evalbot/evalbot_20.png&amp;s=256" class="next-head"><meta itemprop="image" content="https://www.gravatar.com/avatar/a54d14695f564b6539b8ae1bc7fbb2e8?d=https://repl.it/public/images/evalbot/evalbot_20.png&amp;s=256" class="next-head"><meta name="twitter:image" content="https://www.gravatar.com/avatar/a54d14695f564b6539b8ae1bc7fbb2e8?d=https://repl.it/public/images/evalbot/evalbot_20.png&amp;s=256" class="next-head"><style>.grecaptcha-badge:hover { left: 4px !important }</style><style>.grecaptcha-badge:hover { left: 4px !important }</style></head><body class="custom_class"><div id="__next"><div style="position: relative; min-height: 100vh;"><div id="modal-root"></div><div id="page" style="padding-bottom: 0px; padding-top: 0px;"><div class="jsx-3633663456"><div class="jsx-3633663456 email-verification-banner"><span class="jsx-3633663456">Please verify your email. <a class="jsx-3633663456">Resend verification link</a></span></div></div><div class="jsx-1542287934 workspace-page-wrapper"><div class="jsx-3203370839 workspaceWrapper"><div class="jsx-3203370839 windowManagerWrapper"><div style="height: 100%;"><div style="height: 100%; display: flex; flex-direction: column;"><div class="jsx-4022297007" style="height: 60px; width: 100%; position: relative;"><div class="jsx-2212141458 dynamic-header"><div class="jsx-2212141458 dynamic-header-nav-left"><a class="jsx-3261977887 dynamic-header-logo" href="https://repl.it/repls"><img src="./hello_files/icon-square.png" alt="repl.it" class="jsx-3261977887"></a><div class="jsx-4022297007 ws-header"><div class="jsx-1346311872 jsx-2104364215 wrapper"><a href="https://repl.it/@MateoMugen" style="border-bottom: none;"><div class="jsx-3772012161 profile-icon profile-icon-m" style="background-image: url(&quot;https://www.gravatar.com/avatar/a54d14695f564b6539b8ae1bc7fbb2e8?d=https://repl.it/public/images/evalbot/evalbot_20.png&amp;s=256&quot;); margin-right: 10px; width: 32px; height: 32px; flex-shrink: 0;"></div></a><div class="jsx-1346311872 jsx-2104364215 info-wrapper"><div class="jsx-885636785 workspace-header"><div class="jsx-885636785 workspace-header-info"><div class="jsx-885636785 workspace-header-title"><a class="workspace-header-user-link" href="https://repl.it/@MateoMugen">@MateoMugen</a>/SoggyKnobbyProducts</div><div class="jsx-885636785 workspace-header-description-container"><img alt="C++" title="C++" src="./hello_files/cpp.svg" class="jsx-885636785 workspace-header-lang-image"><p class="jsx-885636785">No description</p></div></div></div></div><div class="jsx-47414282 jsx-3138372086 tooltip-base" style="margin-left: 5px; width: 15px; height: 15px;"><div class="jsx-47414282 jsx-3138372086"><div class="jsx-1346311872 jsx-2104364215 header-edit-repl-icon"><svg class="pencil-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10.966 11.017"><defs class="jsx-733959970"></defs><g><path d="M6.86,2.421l-.314-.314L1.581,7.072l2.347,2.37L8.906,4.466,8.6,4.158Z"></path><path d="M10.363,2.393,8.625.654A.445.445,0,0,0,8,.654L7.153,1.5,9.52,3.865l.843-.843A.445.445,0,0,0,10.363,2.393Z"></path><path d="M.524,10.33a.148.148,0,0,0,.187.186l1.821-.661L1.2,8.519Z"></path></g></svg></div></div></div></div><div class="jsx-4022297007 ws-header-buttons"><div class="jsx-415897067 jsx-3939828441 ws-header-cta jsx-3480443222"><span class="jsx-415897067 jsx-3939828441 ws-header-cta-label jsx-3480443222">run</span><span class="jsx-415897067 jsx-3939828441 ws-header-cta-icon jsx-3480443222"><svg class="run-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12.388 14.873"><defs class="jsx-3550419329"></defs><g><path d="M.563,7.439q0-2.973,0-5.946a1.044,1.044,0,0,1,.051-.361A.694.694,0,0,1,1.664.805c.639.372,1.271.752,1.9,1.129q3.879,2.309,7.758,4.62A1.042,1.042,0,0,1,11.507,8.2a.931.931,0,0,1-.171.122Q6.544,11.177,1.75,14.03a.861.861,0,0,1-.63.16.7.7,0,0,1-.556-.716q0-1.609,0-3.22Z"></path></g></svg></span></div><div class="jsx-952725700 jsx-3929440574 share-button-wrapper"><div class="jsx-415897067 jsx-2637703494 ws-header-cta "><span class="jsx-415897067 jsx-2637703494 ws-header-cta-label ">share</span><span class="jsx-415897067 jsx-2637703494 ws-header-cta-icon "><svg class="share-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21.401 16.681"><defs class="jsx-1155514913"></defs><g><path d="M3.215,4.5v9.2H15.442c0-.762.02-1.516-.009-2.268a.86.86,0,0,1,.415-.832c.371-.249.7-.552,1.072-.806a.511.511,0,0,1,.427-.081.538.538,0,0,1,.241.4q.025,2.352,0,4.709a1.063,1.063,0,0,1-1.162,1.046H4.019c-.619,0-1.238,0-1.856,0a1.044,1.044,0,0,1-1.113-1.088q-.006-5.656,0-11.314a1.05,1.05,0,0,1,1.1-1.1c2.293,0,3.485,0,5.777,0,.238,0,.451.041.516.3.073.283-.133.389-.346.512-.634.366-1.248.765-1.88,1.132a1.216,1.216,0,0,1-.562.187c-1.031.018-.963.008-1.994.008Z"></path><path d="M14.6.758l5.833,4.518-5.8,4.5V7.536C11.4,7.295,8.388,7.644,5.74,9.743A7.2,7.2,0,0,1,6.614,7.1,7.877,7.877,0,0,1,11.2,3.6,13.214,13.214,0,0,1,14.366,3a2.124,2.124,0,0,0,.229-.04Z"></path></g></svg></span></div></div></div></div></div><div class="jsx-2212141458 dynamic-header-nav-right"><div class="jsx-2212141458 dynamic-header-nav"><a class="jsx-828026252 jsx-441649983 dynamic-header-nav-item" href="https://repl.it/talk"><div class="dynamic-header-together"><span class="dynamic-header-together-container"><svg class="together-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24.805 16.981"><defs class="jsx-3931840291"></defs><g><path fill="#FFCD0B" class="cls-1" d="M21.5,13.3a5.085,5.085,0,0,0-3.6-2.459,4.73,4.73,0,0,0-2.869,1.443,5.876,5.876,0,0,1,.442,1.016Z"></path><path fill="#FFCD0B" class="cls-1" d="M21.5,13.3a5.085,5.085,0,0,0-3.6-2.459,4.73,4.73,0,0,0-2.869,1.443,5.876,5.876,0,0,1,.442,1.016Z"></path><circle fill="#FFCD0B" class="cls-1" cx="7.743" cy="5.984" r="3.027"></circle><path fill="#FFCD0B" class="cls-1" d="M7.92,11.214a6.011,6.011,0,0,0-4.264,2.83h8.433C11.315,12.654,9.34,11.214,7.92,11.214Z"></path><path fill="#131B32" class="cls-2" d="M10.972,9.98a5.158,5.158,0,1,0-6.331.106c-1.9,1.162-3.514,3.114-3.514,5.049V16.1H14.6v-.961C14.6,13.138,12.919,11.127,10.972,9.98ZM7.744,2.957A3.027,3.027,0,1,1,4.715,5.983,3.027,3.027,0,0,1,7.744,2.957ZM3.656,14.044a6.011,6.011,0,0,1,4.264-2.83c1.42,0,3.394,1.44,4.169,2.83Z"></path><circle fill="#FFCD0B" class="cls-1" cx="17.745" cy="6.463" r="2.488"></circle><path fill="#131B32" class="cls-2" d="M20.538,9.783c-.036-.021-.073-.037-.11-.058a4.242,4.242,0,1,0-5.255.092c-.036.021-.073.037-.108.058a7.96,7.96,0,0,0-1.169.871,7.763,7.763,0,0,1,1.14,1.535A4.731,4.731,0,0,1,17.9,10.838,5.085,5.085,0,0,1,21.5,13.3H15.478a4.778,4.778,0,0,1,.273,1.521v.255h7.927v-.832C23.677,12.514,22.221,10.774,20.538,9.783Zm-2.794-.832a2.488,2.488,0,1,1,2.489-2.487A2.488,2.488,0,0,1,17.744,8.951Z"></path></g></svg></span><span>repl talk</span><style>
      .dynamic-header-together {
        display: flex;
        align-items: center;
        position: relative;
      }
      .dynamic-header-together span {
        margin-left: 5px;
      }
      .dynamic-header-together-container {
        width: 24px;
        height: 16px;
      }
      @media screen and (max-width: 750px) {
        :global(.is-logged-out) .dynamic-header-together {
          display: none;
        }
      }
    </style></div></a><a class="jsx-828026252 jsx-441649983 dynamic-header-nav-item" href="https://repl.it/repls">my repls</a><a href="https://repl.it/community" class="jsx-828026252 jsx-441649983 dynamic-header-nav-item">learn/teach</a><div class="jsx-2212141458 dynamic-header-dropdown"><div class="jsx-1642157231 dynamic-header-dropdown"><div class="jsx-2569052526 dynamic-header-dropdown-label"><div class="jsx-2569052526 dynamic-header-dropdown-username">MateoMugen <span title="cycles" class="jsx-2569052526">(0)</span></div><div class="jsx-2569052526 dynamic-header-dropdown-caret"></div></div></div></div></div></div></div></div><div class="jsx-1280230336 floating-run"></div><div style="height: calc(100% - 60px); width: 100%; display: flex; flex-direction: row;"><div class="jsx-695095782 jsx-2554818929 side-nav" style="width: calc(20% - 5.5px); height: 100%; min-width: 199px;"><div class="jsx-695095782 jsx-2554818929 side-nav-options"><div class="jsx-47414282 jsx-3138372086 tooltip-base"><div class="jsx-47414282 jsx-3138372086"><div class="jsx-942974558 side-nav-item side-nav-item-active"><div class="jsx-942974558 side-nav-item-img"><svg class="file-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 17.908 20.614"><defs class="jsx-588867458"></defs><g><path d="M10.4.937H.9v18.74H17.094V7.608ZM15.6,18.1H2.422V2.51H9.554V8.124H15.6Z"></path></g></svg></div></div></div></div><div class="jsx-47414282 jsx-3138372086 tooltip-base"><div class="jsx-47414282 jsx-3138372086"><div class="jsx-942974558 side-nav-item"><div class="jsx-942974558 side-nav-item-img"><svg class="settings-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.969 21.519"><defs class="jsx-875489994"></defs><g><path d="M18.989,12.813a2.435,2.435,0,0,1-1.257-2.593,1.139,1.139,0,0,1,.45-.891c.5-.356.97-.748,1.44-1.14a2.937,2.937,0,0,0,.359-.436c-.1-.208-.173-.371-.261-.524-.422-.738-.838-1.479-1.276-2.207-.788-1.31-.493-1.316-1.958-.639a2.332,2.332,0,0,1-2.759-.148c-.344-.279-.615-.464-.63-.954a14.7,14.7,0,0,0-.226-1.7.663.663,0,0,0-.757-.648C11.108.957,10.1.943,9.09.943c-.932,0-1,.042-1.082.984C7.9,3.148,7.735,4.328,6.3,4.721a1.448,1.448,0,0,1-.76.071,19.85,19.85,0,0,1-1.873-.74.558.558,0,0,0-.824.289C2.4,5.135,1.927,5.913,1.477,6.7c-.659,1.155-.7,1.227.434,1.966a2.41,2.41,0,0,1,1.253,2.595,1.142,1.142,0,0,1-.456.888c-.513.369-.99.786-1.492,1.172a.506.506,0,0,0-.137.764q.907,1.53,1.78,3.08a.536.536,0,0,0,.783.265q.926-.4,1.871-.748a.82.82,0,0,1,.558-.057,14.7,14.7,0,0,1,1.483.863.63.63,0,0,1,.2.4c.1.622.191,1.247.249,1.873a.738.738,0,0,0,.883.777c.968-.032,1.938-.008,2.907-.009.939,0,1-.045,1.091-.976.115-1.215.252-2.409,1.7-2.8a1.478,1.478,0,0,1,.759-.078,15.994,15.994,0,0,1,1.818.718.6.6,0,0,0,.915-.307c.426-.78.9-1.532,1.327-2.314C20.066,13.571,20.388,13.756,18.989,12.813Zm-5.018-1.841a3.476,3.476,0,0,1-4.144,3.265A3.631,3.631,0,0,1,6.89,10.561,3.533,3.533,0,0,1,10.708,7.22,3.458,3.458,0,0,1,13.971,10.972Z"></path></g></svg></div></div></div></div></div><div class="jsx-695095782 jsx-2554818929 side-nav-active-pane"><div class="jsx-148721707 jsx-2630510 file-tree" style="height: 100%;"><div class="jsx-148721707 jsx-2630510 file-tree-header"><div class="jsx-148721707 jsx-2630510 file-tree-heading">Files</div><div class="jsx-148721707 jsx-2630510 file-tree-actions"><div class="jsx-148721707 jsx-2630510 file-tree-add-icons"><div class="jsx-47414282 jsx-3138372086 tooltip-base"><div class="jsx-47414282 jsx-3138372086"><div class="jsx-148721707 jsx-2630510 file-tree-action-icon-wrapper"><div class="jsx-148721707 jsx-2630510 file-tree-action-icon"><svg class="add-file-icon-svg" data-name="Layer 1 copy 5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34.444 30.299"><defs class="jsx-2225429583"></defs><polygon class="cls-1" points="20.963 1.72 10.572 1.72 10.572 22.234 28.296 22.234 28.296 9.023 20.963 1.72"></polygon><polygon class="cls-2" points="12.235 3.442 12.235 20.512 26.663 20.512 26.663 9.588 20.042 9.588 20.042 3.442 12.235 3.442" style="fill: rgb(255, 255, 255);"></polygon><circle class="cls-3" cx="12.723" cy="21.758" r="6.881" style="display: initial;"></circle><g class="cls-4" style="display: initial;"><path class="cls-2" d="M16.591,22.234H13.332v3.406h-1.1V22.234H8.993v-1.09h3.242V17.738h1.1v3.406h3.259Z"></path></g></svg></div></div></div></div><div class="jsx-148721707 jsx-2630510 file-tree-action-seperator"></div><div class="jsx-47414282 jsx-3138372086 tooltip-base"><div class="jsx-47414282 jsx-3138372086"><div class="jsx-148721707 jsx-2630510 file-tree-action-icon-wrapper"><div class="jsx-148721707 jsx-2630510 file-tree-action-icon"><svg class="add-folder-icon-svg" data-name="add folder icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34.444 30.299"><defs class="jsx-236533324"></defs><rect class="cls-1" x="7.671" y="5.044" width="24.047" height="16.744" style="fill: rgb(255, 255, 255);"></rect><path class="cls-2" d="M29.287,4.12V1.377H20.52V4.12H6.549V23.084h26.3V4.12ZM31.222,21.5H8.116V5.7H22.087V2.958h5.573V5.7h3.561Z"></path><rect class="cls-2" x="20.852" y="2.847" width="7.214" height="2.85"></rect><circle class="cls-3" cx="8.581" cy="22.024" r="6.881" style="display: initial;"></circle><path class="cls-1" d="M12.449,22.5H9.191v3.406h-1.1V22.5H4.851V21.41H8.093V18h1.1V21.41h3.259Z" style="display: initial;"></path></svg></div></div></div></div></div><div class="jsx-1789765924 jsx-800635611"><div class="jsx-1789765924 jsx-800635611 file-tree-options-img-wrapper"><div class="jsx-1789765924 jsx-800635611 file-tree-options-img"><svg id="threedotmenuicon" data-name="Three dots menu" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4.075 17.949" style="height: 100%; width: 100%; display: block;"><circle cx="2.038" cy="2.668" r="1.852" style="fill: currentcolor;"></circle><circle cx="2.038" cy="8.974" r="1.852" style="fill: currentcolor;"></circle><circle cx="2.038" cy="15.28" r="1.852" style="fill: currentcolor;"></circle></svg></div></div><input type="file" multiple="" accept="*" class="jsx-1789765924 jsx-800635611" style="display: none;"><input type="file" webkitdirectory="true" mozdirectory="true" msdirectory="true" odirectory="true" directory="true" accept="*" class="jsx-1789765924 jsx-800635611" style="display: none;"></div></div></div><div class="jsx-148721707 jsx-2630510 file-tree-nodes-wrapper"><div style="background-color: transparent; height: 100%;"><ul class="jsx-2155203631 tree-node-child-list"><li><div class="jsx-279371500 jsx-2820258697 node-row node-row-active" draggable="true"><div class="jsx-279371500 jsx-2820258697 node-row-label"><div class="jsx-1490508611 node-row-icon-container"><div class="jsx-1490508611 node-row-icon"><svg class="add-file-icon-svg" data-name="Layer 1 copy 5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34.444 30.299"><defs class="jsx-2225429583"></defs><polygon class="cls-1" points="20.963 1.72 10.572 1.72 10.572 22.234 28.296 22.234 28.296 9.023 20.963 1.72" style="fill: rgb(255, 255, 255);"></polygon><polygon class="cls-2" points="12.235 3.442 12.235 20.512 26.663 20.512 26.663 9.588 20.042 9.588 20.042 3.442 12.235 3.442" style="fill: rgb(122, 152, 165);"></polygon><circle class="cls-3" cx="12.723" cy="21.758" r="6.881" style="display: none;"></circle><g class="cls-4" style="display: none;"><path class="cls-2" d="M16.591,22.234H13.332v3.406h-1.1V22.234H8.993v-1.09h3.242V17.738h1.1v3.406h3.259Z"></path></g></svg></div></div><span title="main.cpp" class="jsx-279371500 jsx-2820258697 node-row-name">main.cpp</span></div></div></li></ul></div></div></div></div></div><div style="height: 100%; position: relative; display: flex; justify-content: center; align-items: center; flex: 1 0 auto; overflow: hidden; cursor: col-resize; width: 11px; background: rgb(221, 221, 221);"><div style="height: 25px; border-right: 1px solid rgb(119, 120, 121);"></div></div><div style="width: calc(80% - 5.5px); height: 100%; display: flex; flex-direction: row;"><div style="width: calc(50% - 5.5px); height: 100%; display: flex; flex-direction: column;"><div class="jsx-3277473121 file-header" style="height: 32px; width: 100%;"><div class="jsx-3277473121 file-header-name"><div class="jsx-3277473121" style="margin: 0px 30px; padding-right: 0px;">main.cpp</div><div class="jsx-47414282 jsx-3138372086 tooltip-base" style="height: 100%;"><div class="jsx-47414282 jsx-3138372086" style="height: 100%;"><div class="jsx-2396320584 jsx-4280716916 file-header-format-button"><div class="jsx-2396320584 jsx-4280716916 file-header-format-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16.581 16.428" class="jsx-2396320584 jsx-4280716916"><path d="M13.26.747H3.323A2.569,2.569,0,0,0,.754,3.316h0v9.795a2.569,2.569,0,0,0,2.568,2.57h9.937a2.569,2.569,0,0,0,2.569-2.569h0V3.316A2.569,2.569,0,0,0,13.26.747Z" class="jsx-2396320584 jsx-4280716916 cls-1"></path><path d="M13.118,11.269a.759.759,0,0,1-.759.759H3.921a.759.759,0,0,1-.759-.759V11.23a.671.671,0,0,1,.689-.653l.07.006h8.438a.671.671,0,0,1,.753.578.7.7,0,0,1,.006.069ZM3.161,5.111V5.073a.759.759,0,0,1,.759-.759h8.439a.759.759,0,0,1,.759.759v.038a.759.759,0,0,1-.759.759H3.921a.759.759,0,0,1-.76-.758ZM3.148,8.2a.759.759,0,0,1,.758-.76H8.4a.759.759,0,0,1,.759.759v.038a.759.759,0,0,1-.759.759H3.907a.759.759,0,0,1-.759-.759Z" class="jsx-2396320584 jsx-4280716916 cls-2"></path></svg></div></div></div></div></div><div class="jsx-2778461066 jsx-2576527708"><a class="jsx-2778461066 jsx-2576527708 save-status" href="https://repl.it/@MateoMugen/SoggyKnobbyProducts/history"><div class="jsx-2778461066 jsx-2576527708 history-icon"><svg class="history-icon-svg" data-name="Layer 1 copy 5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21.051 18.415"><defs class="jsx-1990457210"></defs><g><path class="cls-1" d="M9.813,6.732a.485.485,0,0,1,.02-.154.262.262,0,0,1,.409-.139c.249.159,2.758,1.8,3.766,2.453a.47.47,0,0,1,.071.7.366.366,0,0,1-.067.052l-3.736,2.436a.314.314,0,0,1-.246.068.3.3,0,0,1-.217-.306C9.813,11.386,9.813,7.578,9.813,6.732Z"></path><path class="cls-2" d="M19.595,7.041A8.324,8.324,0,0,0,18.053,4a8.49,8.49,0,0,0-2.638-2.208A8.3,8.3,0,0,0,12.246.837,8.286,8.286,0,0,0,5.918,2.96,10.2,10.2,0,0,0,3.3,7.162C2.879,6.6,2.362,5.925,2.093,5.568,1.9,5.312,1.9,5.312,1.652,5.5c-.114.087-.228.174-.342.26-.229.171-.229.171-.059.4C2.062,7.23,2.877,8.3,3.679,9.38c.123.165.208.2.394.09,1.184-.683,2.375-1.354,3.564-2.025.032-.018.062-.032.094-.048a.106.106,0,0,0,.045-.147c-.14-.247-.232-.405-.331-.6-.084-.169-.173-.187-.334-.092-.643.375-2.035,1.154-2.083,1.178l-.263.15A10.5,10.5,0,0,1,7.7,3.694a6.579,6.579,0,0,1,3.271-1.133,6.85,6.85,0,0,1,2.847.38,6.353,6.353,0,0,1,2.039,1.195A6.53,6.53,0,0,1,18.1,8.382a6.415,6.415,0,0,1-.465,3.4,6.472,6.472,0,0,1-5.083,3.976,6.43,6.43,0,0,1-2.325-.037,6.538,6.538,0,0,1-2.111-.788,6.094,6.094,0,0,1-1.643-1.4.62.62,0,0,0-.948-.08,2.874,2.874,0,0,1-.278.221.622.622,0,0,0-.124.968,8.162,8.162,0,0,0,1.5,1.377A8.57,8.57,0,0,0,9.387,17.3a8.145,8.145,0,0,0,2.076.273h.089a8.23,8.23,0,0,0,2.72-.487,8.452,8.452,0,0,0,3.954-2.945,8.266,8.266,0,0,0,1.369-7.1ZM4.5,8.032l0-.006h.014Z"></path></g></svg></div><span class="jsx-2778461066 jsx-2576527708">history</span></a></div></div><div class="jsx-3089459507" style="height: calc(100% - 32px); width: 100%; position: relative;"><div class="jsx-1923941960 jsx-3388382399 replit-monaco-editor-container" data-keybinding-context="1" data-mode-id="cpp"><div class="monaco-editor vs" data-uri="file:///home/runner/main.cpp" style="width: 760px; height: 828px;"><div data-mprt="3" class="overflow-guard" style="width: 760px; height: 828px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; will-change: transform; top: 0px; height: 904px; width: 64px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 904px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; width: 64px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; line-height: 19px; letter-spacing: 0px; height: 904px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin current-line-margin-both" style="width:64px; height:19px;"></div><div class="line-numbers" style="left:0px;width:38px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cldr folding" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">3</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">4</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">5</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 64px; width: 696px; height: 828px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; will-change: transform; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 696px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-both" style="width:696px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:15.3984375px"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; line-height: 19px; letter-spacing: 0px; width: 696px; height: 904px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk7">#include</span><span class="mtk1">&nbsp;</span><span class="mtk7">&lt;</span><span class="mtk25">iostream</span><span class="mtk7">&gt;</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk7">int</span><span class="mtk1">&nbsp;main()&nbsp;{</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;std::cout&nbsp;&lt;&lt;&nbsp;</span><span class="mtk25">"Hello&nbsp;World!\n"</span><span class="mtk1">;</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">}</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightbulb-glyph" title="Show Fixes (Ctrl+.)" widgetid="LightBulbWidget" style="position: absolute; visibility: hidden; max-width: 696px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor " style="height: 19px; top: 0px; left: 0px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 682px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; will-change: transform; width: 682px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="828" style="position: absolute; will-change: transform; top: 0px; right: 0px; width: 14px; height: 828px;"></canvas><div role="presentation" aria-hidden="true" class="visible scrollbar vertical" style="position: absolute; width: 14px; height: 828px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; will-change: transform; height: 758px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 760px;"></div><textarea data-mprt="6" class="inputarea" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." role="textbox" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-size: 1px; line-height: 19px; top: 0px; left: 64px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 760px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div class="monaco-editor-hover hidden" aria-hidden="true" role="presentation" widgetid="editor.contrib.modesGlyphHoverWidget" style="position: absolute;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 828px;"><div class="minimap-shadow-hidden" style="height: 828px;"></div><canvas width="1" height="828" style="position: absolute; left: 0px; width: 1px; height: 828px;"></canvas><div class="minimap-slider" style="position: absolute; will-change: transform; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-editor rename-box" widgetid="__renameInputWidget" style="height: 19px; box-shadow: rgb(168, 168, 168) 0px 2px 8px; position: fixed; visibility: hidden; max-width: 1920px;"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; background-color: rgb(255, 255, 255); color: rgb(108, 108, 108); border-width: 0px; border-style: none;"></div><div class="monaco-editor-hover hidden" tabindex="0" widgetid="editor.contrib.modesContentHoverWidget" style="position: fixed; visibility: hidden; max-width: 1920px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-editor-hover-content" style="overflow: hidden; font-size: 14px; line-height: 19px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; will-change: transform;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; will-change: transform;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow top-left-corner"></div></div></div></div><div class="context-view monaco-builder-hidden" aria-hidden="true"></div></div></div></div></div><div style="height: 100%; position: relative; display: flex; justify-content: center; align-items: center; flex: 1 0 auto; overflow: hidden; cursor: col-resize; width: 11px; background: rgb(221, 221, 221);"><div style="height: 25px; border-right: 1px solid rgb(119, 120, 121);"></div></div><div style="width: calc(50% - 5.5px); height: 100%; background-color: rgb(13, 19, 35);"><div class="jsx-3552593814" style="height: 100%; position: relative;"><div class="jsx-3552593814 terminal-opts"><span title="Input" class="jsx-3552593814 input-wrapper"><svg height="20" viewBox="0 0 48 48" width="20" xmlns="http://www.w3.org/2000/svg" class="jsx-3552593814 input-icon"><path d="M0 0h48v48h-48z" fill="none" class="jsx-3552593814"></path><path d="M42 6.02h-36c-2.21 0-4 1.79-4 4v7.98h4v-8.02h36v28.06h-36v-8.04h-4v8.02c0 2.21 1.79 3.96 4 3.96h36c2.21 0 4-1.76 4-3.96v-28c0-2.21-1.79-4-4-4zm-20 25.98l8-8-8-8v6h-20v4h20v6z" class="jsx-3552593814"></path></svg></span><span title="Clear" class="jsx-3552593814 clear-button"></span></div><div id="console" class="jsx-3552593814" style="position: relative; height: 100%;"><div style="position: absolute; left: 25%; right: 25%; top: 47%; height: 7px; background-color: transparent; border-style: solid; border-width: 1px; border-radius: 10px; border-color: rgb(255, 255, 255); transition: opacity 0.5s ease 0s; z-index: 1; opacity: 0;"><div style="width: 100%; height: 5px; background-color: rgb(255, 255, 255);"></div></div><div style="top: 0px; left: 0px; right: 0px; bottom: 0px; position: absolute; overflow: auto;"><pre class="jqconsole jqconsole-blurred" style="margin: 0px; position: relative; min-height: 100%; box-sizing: border-box;"><span class="jqconsole-header"><span class=""></span></span><span><span class="">gcc version 4.6.3
</span></span><span class="jqconsole-old-prompt"><span class="">   
</span></span><span><span class="">Hello World!
</span></span><span class="jqconsole-prompt "><span class="jqconsole-prompt-text"></span><span><span>   </span><span class="jqconsole-prompt-text"></span><span class="jqconsole-cursor" style="color: transparent; display: inline; z-index: 0; position: absolute;">&nbsp;</span><span class="jqconsole-prompt-text" style="position: relative;"></span></span><span class="jqconsole-prompt-text"></span></span></pre><div style="position: absolute; width: 1px; height: 0px; overflow: hidden; left: 30.0781px; top: 65px;"><textarea wrap="off" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" style="position: absolute; width: 2px;"></textarea></div></div></div></div></div></div></div></div><span title="Help" style="background-image: url(&quot;/public/images/help_button_square.svg&quot;); width: 1em; height: 1em; position: absolute; right: 1em; bottom: 1em; cursor: pointer; z-index: 4;"></span></div></div></div></div></div></div></div><div id="__next-error"></div><script>
          __NEXT_DATA__ = {"props":{"pageProps":{"isServer":true,"store":{},"initialState":{"user":{"userInfo":{"fetchState":"idle"},"billingInfo":{"isFetching":false},"authModal":{"promptCount":0,"dismissed":false,"show":false}},"banners":{"message":""},"messages":{"queue":[]},"notifications":{"data":[],"isFetching":false}},"initialProps":{"latestPost":{"title":"Bash Shell Experiment","author":"Rob Blanckaert","url":"shell","date":"Fri Sep 14 2018","content":"\u003cp\u003eRepl\u0026#39;s now provide access to an experimental bash shell via the command palette (\u003ckbd\u003eF1\u003c/kbd\u003e)\u003c/p\u003e\n\u003cp\u003e\u003ca target=\"_blank\" href=\"/public/images/blog/shell.gif\"\u003e\n  \u003cimg src=\"/public/images/blog/shell.gif\" alt=\"shell\" title=\"shell\" /\u003e\n\u003c/a\u003e\u003c/p\u003e\n\u003cp\u003eThe new shell UI uses Xterm.js, an upgraded terminal emulator from the one you are used to for repl output. It supports the full range of vt100 color codes and other commands like listening to mouse clicks. We hope to also bring to these same features to the repl output terminals soon.\u003c/p\u003e\n\u003cp\u003e\u003cstrong\u003eNote:\u003c/strong\u003e Changes to your files made in the shell will NOT be saved back to your repl.\u003c/p\u003e\n\u003cp\u003eThis feature is still a little rough around the edges. Not all commands will work in all languages. If you have any feedback, we would love to hear it on our \u003ca target=\"_blank\" href=\"https://repl.it/feedback/p/xterm-shell\"\u003ecanny board\u003c/a\u003e.\u003c/p\u003e\n","preview":"\u003cp\u003eRepl\u0026#39;s now provide access to an experimental bash shell via the command palette (\u003ckbd\u003eF1\u003c/kbd\u003e)\u003c/p\u003e\n","description":"Repl's now provide access to an experimental bash shell via the command palette (F1)…"}}}},"page":"/","pathname":"/","query":{},"buildId":"941b1f32-e22c-4555-8d90-54dfc2c57b43","assetPrefix":"","nextExport":false,"err":null,"chunks":[]}
          module={}
          __NEXT_LOADED_PAGES__ = []
          __NEXT_LOADED_CHUNKS__ = []

          __NEXT_REGISTER_PAGE = function (route, fn) {
            __NEXT_LOADED_PAGES__.push({ route: route, fn: fn })
          }

          __NEXT_REGISTER_CHUNK = function (chunkName, fn) {
            __NEXT_LOADED_CHUNKS__.push({ chunkName: chunkName, fn: fn })
          }

          false
        </script><script async="" id="__NEXT_PAGE__/" src="./hello_files/index.js.download"></script><script async="" id="__NEXT_PAGE__/_app" src="./hello_files/_app.js.download"></script><script async="" id="__NEXT_PAGE__/_error" src="./hello_files/_error.js.download"></script><script src="./hello_files/main-000e04511466974b7b0d.js.download" async=""></script><script src="./hello_files/auth.js.download"></script><script src="./hello_files/replCreator.js.download"></script><script src="./hello_files/languages.js.download"></script><script src="./hello_files/replEnvironment.js.download"></script><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="status" aria-atomic="true"></div></div></body></html>