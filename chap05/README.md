### Decorate function

- @retry 함수 위에 작성된 것은 run_operation = retry(run_operation) 의 의미이다.

### Decorate Classes

- 함수와 동일하게 class에서도 decorator을 사용할 수 있다. 데코레이터의 파라미터가 class가 된다.
- 1예제는 처음에는 잘동작하지만 다음과 같은 이슈가 생길 수 있다.
    - Too many classes : event가 증가할 수 록 더 많은 클래스가 늘어난다
    - not flexible : 코드를 쉽게 재사용하지 못함
    - Boilerplate : serialize()메서드가 모든 이벤트 클래스에 있어야 한다.

### Other types of decorator

- coroutines : next()를 호출하는 작업은 잊어버리기 쉬운데, 
이 경우 제너레이터를 파라미터로 받아 next()를 호출한 후 제너레이터를 반환하는 데코레이터를 만들면 쉽게 해결된다.

### Passing arguments to decorators
데코레이터가 파라미터를 전달받아 로직을 추상화할 수 있다면 더욱 강력해질것이다. 
파라미터를 갖는 데코레이터는 다음 두 가지 방법으로 구현할 수 있다.
간접 참조를 통해 새로운 레벨의 중첩 함수를 만들어 데코레이터를 한 단계 깊게 만든다.
데코레이터를 위한 클래스를 만든다.
두 번째 방법이 일반적으로 가독성이 더 좋다.


### Decorators with nested functions
파라미터를 데코레이터에 전달하려면 세 단계의 중첩 함수가 필요하다.

첫 번째 함수: 파라미터를 받아서 내부 함수에 전달
두 번째 함수: 데코레이터가 될 함수
세 번째 함수: 데코레이팅 결과 반환 함수

### Decorator ojbects


### Good uses for decorators
4가지가 존재.
- Transforming parameters
- Tracing code
- Validate parameters
- Implement retry operations
- Simplify classes by moving some (repetitive) logic into decorators

### Transforming parameters
데코레이터를 이용하여 파라미터의 유효성을 검사하거나, DbC의 원칙을 따라 사전조건, 사후조건을 강제할 수 있다.
특히 유사한 객체를 반복적으로 생성하거나, 추상화를 위해 유사한 변형을 반복하는 경우 사용하면 좋다.

### Tracing code
여기서 말하는 추적이란 다음과 같은 시나리오에서 사용된다.
- 실제 함수의 실행 경로 추적
- CPU 사용률 등 함수 지표 모니터링
- 함수의 실행 시간 측정
- 언제 함수가 실행되고, 전달된 파라미터는 무엇인지 로깅

### 어디서나 사용할 수 있는 데코레이터
- 함수로 데코레이터 생성시, 클래스 메서드에서 self 인자로 인해 제대로 작동하지 못한다
- 이를 극복하기 위해, 디스크립터 프로토콜을 구현한 데코레이터 객체를 만들 수 있다.(**)