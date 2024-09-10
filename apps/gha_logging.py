import logging
import os

RUNNER_DEBUG = int(os.environ.get("RUNNER_DEBUG", "0"))
ACTIONS_RUNNER_DEBUG = True if "true" == os.environ.get("ACTIONS_RUNNER_DEBUG").lower() else False
ACTIONS_STEP_DEBUG = True if "true" == os.environ.get("ACTIONS_STEP_DEBUG").lower() else False


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG if RUNNER_DEBUG == 1 or ACTIONS_RUNNER_DEBUG else logging.INFO)


logger.info(f"ACTIONS_RUNNER_DEBUG: {ACTIONS_RUNNER_DEBUG}, type: {type(ACTIONS_RUNNER_DEBUG)}")
logger.info(f"ACTIONS_STEP_DEBUG: {ACTIONS_STEP_DEBUG}, type: {type(ACTIONS_STEP_DEBUG)}")


def sub():
    logger.debug("--> sub()")

    for i in range(100):
        logger.debug(f"i={i}")

    logger.debug("<-- sub()")


def main():
    logger.info("--> main()")

    logger.debug("処理を開始します。")
    sub()
    logger.debug("処理が終了しました。")

    logger.info("<-- main()")


if __name__ == "__main__":
    main()
