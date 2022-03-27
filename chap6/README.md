
### Getting More Out of Our Objects With
1. understand what descriptors are, how they work, how to implement 
2. Analyze the two types of descriptors(data and not-data)
3. Reuse code effectively through descriptors
4. Analyze examples of good uses of descriptors and how to take them for our 


### The machinery behind descriptors
- in order to implement descriptors, we need at least two classes
- client class := that is one we want to implement descriptor
- descriptor class := the one that implements the logic of the descriptor


### __get__(self,instance, owner = None)
- `메직메소드 get`은  클래스의 프로퍼티(class property) 또는 클래스 인스턴스의 프로퍼티를 얻기 위해 호출 된다.
- 디스크립터는 클래스 이름을 통한 접근과 객체를 통한 접근 모두 허용 한다. 이로 인해 두가지 인자 instance, owner를 가진다.

### __set__(self, instance, value)
- 인스턴스 attribute의 새 값을 할당할때 call되는 매직메서드이다.


### __delete__(self, instance)
- `del client.descriptor` 와 같은 구문이 실행될떄 , call되는 메직메서드이다.
- 다음 예시는,권리자 권한 없이 함부로 데이터를 삭제하지 못하는 예제를 살펴본다.

