"""
 Map to represent the grfn execution function and original implementation of
 builtin/library functions found in specific languages. Will have structure:
   {
      language: {
            func_name: {
                grfn_implementation: ...
                source_implementation: ...
            }
      }
   }
"""
func_map = {
    "c": {},
    "fortran": {
        "__builtin_max": {"grfn_implementation": "max"},
        "__builtin_sqrtf": {"grfn_implementation": "sqrt"},
        "__builtin_iroundf": {"grfn_implementation": "round"},
        "__builtin_expf": {"grfn_implementation": "exp"},
        "__builtin_cosf": {"grfn_implementation": "cos"},
    },
}


def is_builtin_func(language, name):
    if language not in func_map:
        raise Exception(f"Error: Unknown language in builtins map: {language}")
    language_map = func_map[language]
    return name in language_map


def get_builtin_func_info(language, name):
    if language not in func_map:
        raise Exception(f"Error: Unknown language in builtins map: {language}")

    language_map = func_map[language]
    if name not in language_map:
        raise Exception(
            f'Error: Unknown builtin function for language "{language}": {name}'
        )

    return language_map[name]
