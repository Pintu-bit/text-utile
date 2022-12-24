 <head>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 </head>
 <nav class="navbar navbar-expand-lg bg-dark">
            <div class="container-fluid">
            
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="http://127.0.0.1:8000/">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="about">About</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="textAnyz">textAnyz</a>
                  </li><li class="nav-item">
                    <a class="nav-link" href="#">contact us</a>
                  </li>
                    </ul>
                <form class="d-flex" role="search">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
              </div>
            </div>
          </nav>
<center><h1>Welcome to text analyzer </h1></center>
<center><h2 style="font-family:monospace;"> Your text Analyzer -
{% for prp in purpose %}
{{prp}}{{''}}
{% endfor %}
</h1></center>
<center><h2 style="font-family:monospace;">
{% for i in allcases %}
<div style="width:80%;height:100px;border:solid 1px;background-color:cyan;border-radius:5px;">
   {{i}}
   </div>
   <br><br>
   {% endfor %}
    </h2></center>
