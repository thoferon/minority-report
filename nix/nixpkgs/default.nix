args@{
  extraOverlays ? []
, ...
}:

let
  sources = import ../sources.nix {};

  nixpkgs = import sources.nixpkgs {
    overlays = [
    ] ++ extraOverlays;
  };

in
nixpkgs
