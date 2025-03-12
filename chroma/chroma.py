"""Printing facilities."""

from enum import StrEnum, unique
from types import TracebackType
from typing import IO, Any, Generator, Iterable, Self, Sequence

from rich.box import HORIZONTALS, ROUNDED
from rich.columns import Columns
from rich.console import Console, ConsoleOptions, ConsoleRenderable, RenderableType, RenderResult
from rich.panel import Panel
from rich.pretty import pretty_repr
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    ProgressType,
    SpinnerColumn,
    TaskID,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.rule import Rule
from rich.table import Table as RichTable
from rich.text import Text
from rich.theme import Theme

_theme = Theme(
    {
        "heading1": "bold bright_white",
        "heading2": "bold underline bright_white",
        "heading3": "bold bright_white",
        "error": "deep_pink2",
        "warning": "gold1",
        "success": "green_yellow",
        "info": "light_cyan1",
        "emphasis": "italic bright_white",
        "text": "",
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
    "heading1": "",
    "heading2": "",
    "heading3": "",
    "error": "✖",
    "warning": "⚠",
    "success": "🗹",
    "info": "🛈",
    "emphasis": "",
    "text": "",
}
"""The default icons."""
_console = Console(theme=_theme, markup=False)
"""The default console."""


@unique
class Level(StrEnum):
    """The print level."""

    HEADING1 = "heading1"
    """Heading 1 level."""
    HEADING2 = "heading2"
    """Heading 2 level."""
    HEADING3 = "heading3"
    """Heading 3 level."""
    ERROR = "error"
    """Error level."""
    WARNING = "warning"
    """Warning level."""
    SUCCESS = "success"
    """Success level."""
    INFO = "info"
    """Informational level."""
    EMPHASIS = "emphasis"
    """Emphasis level."""
    TEXT = "text"
    """Text level."""


def pprint(
    *objects: Any,
    file: IO[str] | None = None,
    level: Level = Level.INFO,
    highlight: bool = False,
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
        console = Console(theme=_theme, file=file)
    icon = _icons[level]

    if len(objects) == 0:
        console.print()
        return

    if level in Level.ERROR:
        objects = [Panel(*objects, box=ROUNDED, expand=False)]
    else:
        if icon:
            objects = [_icons[level], *objects]

    if level == Level.HEADING1:
        console.print()
    console.print(*objects, style=level, highlight=highlight)
    if level == Level.HEADING1:
        console.print(Rule(style="dim white"))


class Table(ConsoleRenderable):  # pylint: disable=too-few-public-methods
    """A table."""

    def __init__(self, *columns: Sequence[str], title: str | None = None, highlight: bool = False) -> None:
        """
        Create the table.

        :param columns: The names of the table columns.
        :param title: The title of the table.
        :param highlight: Toggle the data highlighting.
        """
        self._table = RichTable(*columns, box=HORIZONTALS, title=title, highlight=highlight)

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
    """A table for printing key-value pairs."""

    def __init__(self, title: str | None = None, highlight: bool = False) -> None:
        """
        Create the table.

        :param title: The title of the table.
        :param highlight: Toggle the data highlighting.
        """
        super().__init__("key", "value", title=title, highlight=highlight)
        self._table.show_header = False
        self._table.pad_edge = False
        self._table.show_edge = False


class _ProgressBar(Progress):  # pylint: disable=too-few-public-methods
    """A custom progress bar."""

    def __init__(self, *, description: str = "", table: Table | None = None) -> None:
        """Create the progress bar."""
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
        self.start()

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
    """A progress bar."""

    def __init__(
        self,
        sequence: Iterable[ProgressType] | None = None,
        *,
        description: str = "",
        table: Table | None = None,
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

    def __iter__(self) -> Generator[ProgressType]:
        """
        Iterate the sequence.
        :return: The next element of the sequence.
        """
        with self.__progress:
            yield from self.__progress.track(self.__sequence, description=self.__description)

    def add_task(self, *, description: str, total: float = 0) -> TaskID:
        """
        Add a new task.
        :param description: the task description
        :param total: the number of steps
        :return: the task ID
        """
        return self.__progress.add_task(description, total=total)

    def remove_task(self, task_id: TaskID) -> None:
        """
        Remove a new task.
        :param task_id: the task ID
        """
        return self.__progress.remove_task(task_id)

    def update_task(self, task_id: TaskID, *, description: str | None = None, advance: float = 1) -> None:
        """
        Update a task
        :param task_id: the task ID
        :param description: the task description; set to None to not change it
        :param advance: the advancement
        """
        self.__progress.update(task_id=task_id, advance=advance, description=description)

    def __enter__(self) -> Self:
        """
        The enter action for the context manager.
        :return: itself
        """
        return self

    def __exit__(
        self,
        execution_type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> None:
        """
        The exit action for the context manager.
        :param execution_type: the exception type
        :param value: the exception value
        :param traceback: the traceback
        """
        self.__progress.stop()
