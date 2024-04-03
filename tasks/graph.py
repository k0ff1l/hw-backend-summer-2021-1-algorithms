from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        ans = []
        stack = [self._root]
        visited = set()
        while stack:
            i = stack.pop()
            # write dfs
            if i not in visited:
                visited.add(i)
                ans.append(i)
                stack.extend(i.outbound[::-1])
        return ans

    def bfs(self) -> list[Node]:
        ans = []
        stack = [self._root]
        visited = set()
        for i in stack:
            if i not in visited:
                visited.add(i)
                ans.append(i)
                stack.extend(i.outbound)
        return ans
