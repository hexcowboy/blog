Title: CSS
Date: 2015-12-03 10:20
Category: Review
Description: This is a basic description.

edited

```css
@font-face {
    font-family: CaminoBold;
    src: url('../fonts/ElCamino-Bold.otf');
}

@font-face {
    font-family: CaminoSlim;
    src: url('../fonts/ElCamino-Slim.otf');
}

html, body {
  margin: 0;
  padding: 0;
  max-width: 100%;
  overflow-x: hidden;
  background-color: #222831;
  color: #ececec;
}

::selection {
  background: #30475e;
  padding: 5px;
}

button,
a.button {
  color: #ececec;
  background-color: #30475e;

  font-family: soleil,sans-serif;
  font-weight: 500;
  font-style: normal;
  text-decoration: none;
  text-align: center;
  user-select: none;

  padding: 20px;
  margin: 10px;
  border-radius: 10px;

  cursor: pointer;
}

/* Header */

header, footer {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  padding-left: 30px;
  padding-right: 30px;
}

header {
  align-items: center;
  flex-wrap: wrap;
}

header #title h1,
header #title h1 a,
header #title h1 a:visited,
header #title h1 a:active,
header #title h1 a:hover {
  margin: 0;
  font-family: CaminoBold, sans-serif;
  font-weight: 800;
  font-style: normal;
  font-size: 3rem;
  line-height: 1;
  text-align: center;
  text-decoration: none;
  color: white;
  white-space: nowrap;
}

/* Content */

.content {
  margin-top: 24px;
}

#articles {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

#articles .article {
  display: flex;
  margin-bottom: 20px;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
}

#articles .article .cover {
  width: 100%;
}

.cover {
  border-radius: 10px;
}

#articles .article .title {
  margin: 0;
  font-family: soleil,sans-serif;
  font-weight: 700;
  font-style: normal;
  order: 1;
}

#articles .article,
#articles .article:hover,
#articles .article:visited,
#articles .article:active {
  color: white;
  text-decoration: none;
}

#articles .article .date {
  font-family: soleil,sans-serif;
  font-weight: 300;
  font-style: normal;
  font-size: 14px;
  color: #ececec;
  margin-bottom: 4px;
}

.article-title {
  line-height: 1;
  margin: 0;
}

.article-body {
  max-width: 40rem;
  padding: 3rem;
  padding-top: 0;
  padding-left: 6rem;
  padding-right: 6rem;
  margin-left: auto;
  margin-right: auto;
  font-family: sans-serif;
  font-weight: 300;
  font-style: normal;
  font-size: 24px;
  line-height: 30px;
}

.article-body *
:not(li)
:not(.codehilite *) {
  display: flex;
  flex-direction: column;
  overflow: visible;
}

.article-info,
.article-info * {
  display: inline !important;
}

.article-body small {
  font-size: 10px;
  padding-bottom: 1rem;
  display: block;
}

.article-body .article-info {
  margin: 0;
  margin-top: 20px;
  font-family: soleil,sans-serif;
  font-weight: 300;
  font-style: normal;
  font-size: 12px;
  text-align: center;
}

.article-body .article-info .author {
  color: white;
}

.article-body a {
  color: white;
}

.article-body * img {
  max-width: calc(100% + 12rem);
  margin-left: -6rem;
}

.article-body code
:not(.codehilite *) {
  font-family: 'SF Pro', 'Fira Code', monospace;
  font-size: 1rem;
  white-space: nowrap;
  overflow-x: auto;
}

.article-body pre {
  padding: 24px;
  max-width: 100%;
  overflow: scroll;
  font-size: 14px;
  line-height: 20px;
}

/* Pagination */

.pagination {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 2rem;
  padding-left: 60px;
  padding-right: 60px;
}

.pagination a.button {
  min-width: 4rem;
  width: 7rem;
}

.pagination .prev {
  align-self: flex-start;
  margin-right: auto;
}

.pagination .spacer {
  width: 10px;
}

.pagination .next {
  align-self: end;
  margin-left: auto;
}

/* Subscribe block */

#subscribe {
  padding: 60px;
  display: flex;
  justify-content: center;
}

#subscribe h1 {
  margin: 10px;
}

#subscribe h2 {
  font-family: span,serif;
  font-weight: 700;
  font-style: normal;
  margin: 10px;
}

.form-inline {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
}

.form-inline label {
  display: none;
}

.form-inline input,
.form-inline button {
  font-family: soleil,sans-serif;
  font-weight: 300;
  font-style: normal;
  padding: 20px;
  margin: 10px;
  border: 1px solid darkslategray;
}

.form-inline input {
  width: 20rem;
}

.form-inline input:focus,
.form-inline button:focus {
  outline: 2px solid darkblue !important;
  border: 1px solid darkblue;
}

.form-inline button {
  border-radius: 0;
  background-color: darkblue;
  color: white;
}

.form-inline button:hover {
  cursor: pointer;
}

/* Footer */

footer {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: top;
  background-color: #30475e;
  color: #ececec;
  padding: 60px;
}

footer ::selection {
  background-color: #222831;
}

#footer-title {
  flex-basis: 30rem;
  display: block;
}

#footer-links {
  flex-basis: 30rem;
  margin-top: 0 !important;
  display: flex;
  max-width: 100%;
}

#footer-links div {
  width: 15rem;
}

footer h2 {
  margin-bottom: 20px;
  font-family: soleil, sans-serif;
  font-weight: 300;
  font-style: normal;
  line-height: 1;
}

footer .title {
  font-family: CaminoBold;
  font-size: 46px;
  font-weight: 800;
  text-decoration: none;
  margin-top: 0;
}

footer a,
footer a:hover,
footer a:visited,
footer a:active {
  color: #ececec;
}

/* Responsiveness */

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (max-width: 767px) {
  header {
    height: 10vh;
  }

  #articles .article .title {
    font-size: 30px;
  }

  .article-body {
    font-size: 22px;
    padding-left: 3rem;
    padding-right: 3rem;
  }

  .article-body img {
    margin-left: -4rem;
    width: calc(100% + 8rem);
  }

  #footer-links {
    flex-direction: column;
  }

  .pagination {
    padding: 20px;
  }
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
  header {
    padding-left: 60px;
    padding-right: 60px;
  }

  #articles .article {
    width: 44%;
  }
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
  #articles .article {
    width: 28%;
  }
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
  header #title {
    font-size: 24px;
  }

  .content {
    margin-left: 60px;
    margin-right: 60px;
  }

  #articles .article {
    width: 28%;
  }
}

/* XXL devices */
@media only screen and (min-width: 1400px) {
  #articles .article {
    width: 21%;
  }
}
```