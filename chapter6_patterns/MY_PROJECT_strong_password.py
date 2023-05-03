import re


def strong_check(password: any):
    password_regex = re.compile(
        r"""
        ^               # start 
        (?=.*[a-z])   # at least contain lowercase   
        (?=.*[A-Z])   # at least contain lowercase   
        (?=.*[\d])   # at least contain lowercase   
        (?=.*[\/\.#@\$])   # at least contain lowercase   
        (?=.*[a-z])   # at least contain lowercase
        .{8,}
        $               # end
    """,
        re.VERBOSE | re.DOTALL,
    )
    return password_regex.match(password)


text = "usManKha\n9@"
show = strong_check(text)
print(show)
