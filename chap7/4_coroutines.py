# 코루틴 예시
import logging


def stream_db_records(db_handler):
    try:
        while True:
            yield db_handler.read_n.records(10)
    except GeneratorExit:
        db_handler.close()


# 위 예시에서는 제너레이터를 호출할 때마다 데이터베이스 핸들러에서
# 얻은 레코드를 10개씩 반환하고, close()를 호출하면 데이터베이스 연결도 함께 종료한다.


# throw


class CustomException:
    pass


def stream_data(db_handler):
    while True:
        try:
            yield db_handler.read_n.records(10)
        except CustomException as e:
            logging.error(f"처리할 수 있는 {e}")
        except Exception as e:
            logging.error(f"처리할 수 없는 {e}")
            db_handler.close()
            break
