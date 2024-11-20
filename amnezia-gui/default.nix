{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    gtk3
    python312Packages.tkinter
    python312Packages.pygobject3
  ];
}

