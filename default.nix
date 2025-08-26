
{ pkgs ? import <nixpkgs> { config.allowUnfree = true; } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    poetry
	  python313Full
    python313Packages.matplotlib
  ];
  shellHook = ''
	  
  '';
}
