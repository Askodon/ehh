{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  pname = "ehh";
  version = "1.0";

  # nix-prefetch-github askodon ehh
  src = pkgs.fetchFromGitHub {
    owner = "Askodon";
    repo = "ehh";
    rev = "main"; 
    sha256 = "sha256-Ay0yQ3QGDqUeEc/LCmKjuxR/XFNvZQAXjv8cWN5MnUs="; 
  };

  propagatedUserEnvPkgs = [ pkgs.gum pkgs.just pkgs.lua ];
  
  installPhase = ''
    mkdir -p $out/bin
    cp ehh $out/bin/ehh
    chmod +x $out/bin/ehh
  '';
}

