#include "lualilka_util.h"

namespace lilka {

int lualilka_util_delay(lua_State* L) {
    float s = luaL_checknumber(L, 1);
    delayMicroseconds(s * 1000000);
    return 0;
}

static const luaL_Reg lualilka_util[] = {
    {"delay", lualilka_util_delay},
    {NULL, NULL},
};

// int luaopen_lilka_util(lua_State* L) {
//     luaL_newlib(L, lualilka_util);
//     return 1;
// }

int lualilka_util_register(lua_State* L) {
    // Create global "util" table that contains all util functions
    luaL_newlib(L, lualilka_util);
    lua_setglobal(L, "util");
    return 0;
}

} // namespace lilka
