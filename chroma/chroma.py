"""Printing facilities."""

from enum import StrEnum, unique
from typing import Any, IO, Iterable, Sequence

from rich.box import SIMPLE_HEAD
from rich.columns import Columns
from rich.console import Console, ConsoleOptions, ConsoleRenderable, RenderResult, RenderableType
from rich.panel import Panel
from rich.pretty import pretty_repr
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    ProgressType,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.table import Table as RichTable
from rich.text import Text
from rich.theme import Theme

_theme = Theme(
    {
        "debug": "italic gray50",
        "info": "",
        "notice": "bold italic bright_white",
        "success": "green_yellow",
        "warning": "gold1",
        "error": "deep_pink2",
        "critical": "bold italic deep_pink2",
        "alert": "deep_pink2",
        "emergency": "bold italic deep_pink2",
        "repr.ellipsis": "dark_goldenrod",
        "repr.path": "medium_purple3",
        "repr.filename": "medium_purple1",
        "repr.url": "underline deep_sky_blue3",
        "repr.ipv4": "sea_green3",
        "repr.ipv6": "sea_green3",
        "repr.uuid": "light_goldenrod3",
        "repr.none": "medium_orchid",
        "repr.bool_true": "medium_orchid1",
        "repr.bool_false": "medium_orchid1",
        "repr.str": "sea_green2",
        "repr.number": "dark_olive_green1",
        "bar.back": "grey23",
        "bar.complete": "deep_pink2",
        "bar.finished": "green_yellow",
        "progress.download": "cornsilk1",
        "progress.percentage": "wheat1",
        "progress.remaining": "khaki1",
        "progress.elapsed": "dark_olive_green1",
        "progress.spinner": "deep_pink1",
    }
)
"""The default theme."""
_icons = {
    "debug": "",
    "info": "",
    "notice": "",
    "success": "✔",
    "warning": "❇",
    "error": "✖",
    "critical": "✖",
    "alert": "✖",
    "emergency": "✖",
}
"""The default icons."""
_console = Console(theme=_theme, markup=False)
"""The default console."""


@unique
class Level(StrEnum):
    """
    The print level.
    """

    DEBUG = "debug"
    """Debugging level."""
    INFO = "info"
    """Informational level."""
    NOTICE = "notice"
    """Notice level."""
    SUCCESS = "success"
    """Success level."""
    WARNING = "warning"
    """Warning level."""
    ERROR = "error"
    """Error level."""
    CRITICAL = "critical"
    """Critical level."""
    ALERT = "alert"
    """Alert level."""
    EMERGENCY = "emergency"
    """Emergency level."""


def pprint(
    *objects: Any, file: IO[str] | None = None, level: Level = Level.INFO, highlight: bool = False
) -> None:
    """
    Pretty print various objects.

    :param objects: The objects to print.
    :param file: The file to write to; set to `None` for `stdout`.
    :param level: The message level.
    :param highlight: Toggle the data highlighting.
    """
    if file is None:
        console = _console
    else:
        console = Console(theme=_theme, markup=False, file=file)
    icon = _icons[level]

    if level == Level.EMERGENCY:
        objects = [
            Panel(*objects, title=f"{_icons[level]} Emergency {_icons[level]}", expand=False)
        ]
    elif level == Level.ALERT:
        objects = [Panel(*objects, title=f"{_icons[level]} Alert {_icons[level]}", expand=False)]
    else:
        if icon:
            objects = [_icons[level], *objects]

    console.print(*objects, style=level, highlight=highlight)


class Table(ConsoleRenderable):
    """
    A table.
    """

    def __init__(self, *columns: Sequence[str], highlight: bool = False) -> None:
        """
        Create the table.

        :param columns: The names of the table columns.
        :param highlight: Toggle the data highlighting.
        """
        self._table = RichTable(*columns, box=SIMPLE_HEAD, highlight=highlight)

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """
        Render the table.

        :param console: The console to use.
        :param options: The options for the console.
        :return: A render result.
        """
        return self._table.__rich_console__(console, options)

    def add(self, *row: Any, level: Level = Level.INFO) -> None:
        """
        Add a new row.

        :param row: The row elements.
        :param level: The row level.
        """
        elements = []
        for i in row:
            text = pretty_repr(i) if not isinstance(i, str) else i
            if level != Level.INFO:
                text = Text(text, style=level)
            elements.append(text)
        self._table.add_row(*elements)


class KeyValueTable(Table):  # pylint: disable=too-few-public-methods
    """
    A table for printing key-value pairs.
    """

    def __init__(self, highlight: bool = False) -> None:
        """
            Create the table.

        :param highlight: Toggle the data highlighting.
        """
        super().__init__("key", "value", highlight=highlight)
        self._table.show_header = False
        self._table.pad_edge = False
        self._table.show_edge = False


class _ProgressBar(Progress):  # pylint: disable=too-few-public-methods
    """
    A custom progress bar.
    """

    def __init__(self, *, description: str = "", table: Table | None = None) -> None:
        """
        Create the progress bar.
        """
        columns = [SpinnerColumn(finished_text=Text("✔", style="progress.elapsed"))]
        if description:
            columns.append(TextColumn("[progress.description]{task.description}"))
        columns.extend(
            [
                BarColumn(bar_width=None),
                MofNCompleteColumn(),
                TaskProgressColumn(show_speed=True),
                TimeRemainingColumn(elapsed_when_finished=True),
            ]
        )
        self.__table = table
        super().__init__(*columns, console=_console)
        self.live.vertical_overflow = "visible"

    def get_renderables(self) -> Iterable[RenderableType]:
        """
        Retrieve the renderables of the progress bar.

        :return: The renderables of the progress bar.
        """
        bar_renderable = self.make_tasks_table(self.tasks)
        if self.__table is None:
            renderable = bar_renderable
        else:
            renderable = Columns((self.__table, bar_renderable), align="left", expand=True)
        yield renderable


class ProgressBar(Iterable[ProgressType]):  # pylint: disable=too-few-public-methods
    """
    A progress bar.
    """

    def __init__(
        self, sequence: Iterable[ProgressType], *, description: str = "", table: Table | None = None
    ) -> None:
        """
        Create the progress bar.

        :param sequence: The sequence to iterate.
        :param description: The optional description of the progress bar.
        :param table: An optional table to show with the progress bar.
        """
        self.__progress = _ProgressBar(description=description, table=table)
        self.__sequence = sequence
        self.__description = description

    def __iter__(self) -> ProgressType:
        """
        Iterate the sequence.

        :return: The next element of the sequence.
        """
        with self.__progress:
            yield from self.__progress.track(self.__sequence, description=self.__description)
