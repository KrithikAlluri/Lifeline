import { fileURLToPath } from "node:url";
import { loadEnv } from "vite";
const isValidIdentifierRe = /^[_$a-zA-Z][\w$]*$/;
function getPrivateEnv(fullEnv, astroConfig, useRawValues) {
  const viteConfig = astroConfig.vite;
  let envPrefixes = ["PUBLIC_"];
  if (viteConfig.envPrefix) {
    envPrefixes = Array.isArray(viteConfig.envPrefix) ? viteConfig.envPrefix : [viteConfig.envPrefix];
  }
  const privateEnv = {};
  for (const key in fullEnv) {
    if (isValidIdentifierRe.test(key) && envPrefixes.every((prefix) => !key.startsWith(prefix))) {
      if (typeof process.env[key] !== "undefined") {
        let value = process.env[key];
        if (typeof value !== "string") {
          value = `${value}`;
        }
        if (!useRawValues && (value === "0" || value === "1" || value === "true" || value === "false")) {
          privateEnv[key] = value;
        } else {
          privateEnv[key] = `process.env.${key}`;
        }
      } else {
        privateEnv[key] = JSON.stringify(fullEnv[key]);
      }
    }
  }
  return privateEnv;
}
function getEnv(mode, config, useRawValues) {
  const loaded = loadEnv(mode, config.vite.envDir ?? fileURLToPath(config.root), "");
  const privateEnv = getPrivateEnv(loaded, config, useRawValues);
  return { loaded, privateEnv };
}
const createEnvLoader = (mode, config, useRawValues) => {
  let { loaded, privateEnv } = getEnv(mode, config, useRawValues);
  return {
    get: () => {
      ({ loaded, privateEnv } = getEnv(mode, config, useRawValues));
      return loaded;
    },
    getPrivateEnv: () => privateEnv
  };
};
export {
  createEnvLoader
};
