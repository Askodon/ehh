#!/usr/bin/env lua
print([[ 
  ______ _     _       __  __
 |  ____| |   | |     |  \/  |                 
 | |__  | |__ | |__   | \  / | ___ _ __  _   _ 
 |  __| | '_ \| '_ \  | |\/| |/ _ \ '_ \| | | |
 | |____| | | | | | | | |  | |  __/ | | | |_| |
 |______|_| |_|_| |_| |_|  |_|\___|_| |_|\__,_|  
]])

local path = "/home/askodon/nixos-conf/"

-- Func to execute and get stdout
function run_command(command)
    local handle = io.popen(command)
    local result = handle:read("*a")
    handle:close()
    return result
end

local output = run_command("cd " .. path .. " && just | sed 's/Available//g; s/recipes://g'")

local command = "echo '" .. output .. "' | gum choose"
local selected_task = run_command(command)

selected_task = selected_task:gsub("%s+", "") -- Remove spaces
selected_task = selected_task:gsub("\n", "")

if selected_task ~= "" then
    run_command("cd " .. path .. " && just " .. selected_task)
else
    print("Не выбрана ни одна задача.")
end
