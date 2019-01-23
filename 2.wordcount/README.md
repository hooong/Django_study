# 템플릿 언어

- 템플릿 변수 `{{value}}`

- 템플릿 필터 `{{value | filter}}`  ex)`{{value | length}}`

- 템플릿 태그 `{% tag %}...태그내용...{% endtag %}`

  ​		   `{%url 'url_name'%}`  url을 표시해준다.

```python
{% for ------ %}
 #반복할 내용
{% endfor %}
```

### views.py에서 template로 변수 넘기기

`    return render(request, 'result.html', {'full': text, 'total': len(words)})`

- render를 해줄때 맨 마지막 인자로 'key-value'형식으로 넘겨준다.

- 여기서 `key`값이 template에서 템플릿에서 사용된다.


## Staticfiles Managing

1. `app`폴더에 `static`폴더를 생성
   - static 폴더 안에 `css`나 `js` 또는 `image` 처럼 필요한 폴더를 또 생성한다.
   - 예제에서는 `css/basic.css`를 생성한다.
2. `css`를 사용 할 `html`문서 맨 위 (즉, `<head>`태그 위)에 `{% load static %}`을 추가
3. `<head></head>`에 `<link rel="stylesheet" type="text/css" href="{% static 'css/basic.css' %}">`추가
4. 서버가 켜져있었다면 서버를 껐다가 다시 킨다.
   - 서버 끄기는 (`ctrl`+`c`)
   - 서버 켜기는 `$ python manage.py runserver`
