<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dropdown</title>
</head>
<body>
<select name="color" method="GET" action="/">
  <option value="{{colors[0]}}" selected>{{colors[0]}}</option>
  {% for colour in colours[1:] %}
    <option value="{{color}}">{{color}}</option>
  {% endfor %}
</select>

</body>
</html>