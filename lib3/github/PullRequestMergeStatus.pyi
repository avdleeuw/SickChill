from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class PullRequestMergeStatus(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def merged(self) -> bool: ...
    @property
    def message(self) -> str: ...
    @property
    def sha(self) -> str: ...
