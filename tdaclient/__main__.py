from tdaclient.td.lock_error import LockError
from tdaclient.td.tdlock import TDLock
import time
import logging
import tdaclient.td.config as config

logging.basicConfig(
    level=config.get_logging_level(), format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)


def main(argv: list[str]) -> None:
    tdlock = TDLock()
    try:
        lock = tdlock.wait_and_acquire_lock("test", timeout_seconds=30)
        print("sleeping")
        time.sleep(6)
        print("releasing lock")
        tdlock.release_lock(lock)
    except LockError as e:
        print(e)

    print("Goodbye")
    # tdsession = TDSession(session_id="TEST")
    # tdsession.auth()
    # response = tdsession.userprincipal()
    # print(response)


if __name__ == "__main__":
    main(["cat"])
