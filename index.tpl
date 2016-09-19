<html>
    <head>
      <link href="http://mincss.com/entireframework.min.css" rel="stylesheet" type="text/css">
    </head>
    <body>
      <div class="row">
        <div class="col c4"></div>
        <div class="col c4" style="left: 33%; position: absolute">
          %if result:
            <div class="msg">
              <b>Result:</b> {{result}}
            </div><br />
            <form action="/vote" method="post" enctype="multipart/form-data">
              What do you think?<br />
              <textarea name="thought" readonly="true" style="width: 100%" class="smooth">{{text}}</textarea><br />
              Is it right?<br />
              <div class="row">
                <div class="col c6">
                  <select name="vote" style="width: 130px">
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                  </select>
                </div>
                <div class="col c6">
                  <input type="submit" class="btn btn-b" value="Vote" />
                </div>
            </form>
          %else:
            <form action="/think" method="post" enctype="multipart/form-data">
              What do you think?<br />
              <textarea name="thought" class="smooth" style="width: 100%" /></textarea><br />
              <input type="submit" class="btn btn-b smooth" value="Am I sad?" />
            </form>
          %end
          {{message}}
        </div>
        <div class="col c4"></div>
      </div>
    </body>
</html>
