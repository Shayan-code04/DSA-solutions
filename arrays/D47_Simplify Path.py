class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split the path by '/'
        for part in path.split("/"):

            # Ignore empty strings and current directory
            if part == "" or part == ".":
                continue

            # Go back one directory
            elif part == "..":
                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        # Build the simplified path
        return "/" + "/".join(stack)
    