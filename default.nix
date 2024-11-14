{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  pname = "ehh";
  version = "1.0";

  # nix-prefetch-github askodon ehh
  src = pkgs.fetchFromGitHub {
    owner = "Askodon";
    repo = "ehh";
    rev = "main"; 
    sha256 = "sha256-KwLNMXMXIUcgKluTG6RBv1kGgfxQd4GGbTC5k6T/8u4="; 
  };

  propagatedUserEnvPkgs = [ pkgs.gum pkgs.just pkgs.lua ];
  
  installPhase = ''
    mkdir -p $out/bin
    cp ehh $out/bin/ehh
    chmod +x $out/bin/ehh
  '';
}

