#Faker

> 가짜데이터를 생성해주는 pip패키지.
>
> 왜 필요한가? -> 데이터가 많은 상황을 염두해 그 상황을 재현해볼때 사용한다.

1. 가상환경을 실행해준다.

2. `$ pip install faker` - faker를 설치한다.

3. `from faker import Faker` - faker를 import해준다.

4. `fake = Faker()` - Faker객체를 생성

   - `fake = Faker('ko_KR')` - 한국어 가짜데이터를 생성할 때

5. 각 메서드를 통해 데이터의 종류를 결정지을 수 있다.

6. ```python
   print(fake.name())
   print(fake.address())
   print(fake.text())
   print(fake.state())
   print(fake.sentence())
   print(fake.random_number())
   ```

6. `fake.seed(seed객체 번호)` - 저장된 가짜데이터를 불러올 수 있다.

----

- faker공식문서

  > https://pypi.org/project/Faker/



# End

