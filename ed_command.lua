#!/usr/bin/env lua

local function run_command(command)
    local handle = io.popen(command)
    local result = handle:read("*a")
    handle:close()
    return result
end

local editor_options = "nvim\ncode\nnano"
local editor_command = "echo -e \"" .. editor_options .. "\" | gum choose --limit 1"
local editor = run_command(editor_command):gsub("%s+", "") -- Remove spaces

if editor == "" then
    print("Error: editor is not confirm.")
    os.exit(1)
end

local input = run_command("gum filter")

os.execute(editor .. " " .. input)

