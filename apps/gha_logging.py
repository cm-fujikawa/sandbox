import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


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
