import pkg_resources

version = pkg_resources.require("biosniff")[0].version


from .sniffer import Sniffer

import colorlog

colors = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}


formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s[%(name)s:%(lineno)d]: %(reset)s %({})s%(message)s".format(
        "green"
    ),
    datefmt=None,
    reset=True,
    log_colors=colors,
    secondary_log_colors={},
    style="%",
)

logger = colorlog.getLogger("biosniff")
handler = colorlog.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
