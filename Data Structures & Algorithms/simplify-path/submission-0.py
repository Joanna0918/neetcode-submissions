class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        res = []

        for f in path_list:
            if f == "" or f == ".":
                continue
            if f == "..":
                if res:
                    res.pop()
                else:
                    continue
            else:
                res.append(f)

        return "/" + "/".join(res)