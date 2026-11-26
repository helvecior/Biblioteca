"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.readSettings = readSettings;
const unknown_1 = require("./unknown");
/**
 * Checks the better-comments settings. They come from settings.json, so they can hold any JSON value: the schema
 * in package.json only says tags is an array, so VS Code passes on whatever the items contain.
 * - Flags are only ever tested for truthiness, so any value is read as a boolean.
 * - A colour is kept if it's a string or a theme colour ({ "id": "editorError.foreground" }), the shapes VS Code can
 *   use. Anything else is dropped.
 * - A tag without a string tag is skipped, and tags that aren't a list give none. Up to 3.1.1 either stopped the
 *   extension loading (#552). An incomplete tag is normal while settings.json is being edited, so nothing is reported.
 * @param raw The value of vscode.workspace.getConfiguration('better-comments')
 */
function readSettings(raw) {
    const tags = (0, unknown_1.property)(raw, 'tags');
    const list = Array.isArray(tags) ? tags : [];
    return {
        tags: list.map(readTag).filter(tag => tag !== undefined),
        multilineComments: Boolean((0, unknown_1.property)(raw, 'multilineComments')),
        highlightPlainText: Boolean((0, unknown_1.property)(raw, 'highlightPlainText')),
    };
}
function readTag(item) {
    const tag = (0, unknown_1.property)(item, 'tag');
    if (typeof tag !== 'string') {
        return undefined;
    }
    return {
        tag,
        color: readColor((0, unknown_1.property)(item, 'color')),
        backgroundColor: readColor((0, unknown_1.property)(item, 'backgroundColor')),
        strikethrough: Boolean((0, unknown_1.property)(item, 'strikethrough')),
        underline: Boolean((0, unknown_1.property)(item, 'underline')),
        bold: Boolean((0, unknown_1.property)(item, 'bold')),
        italic: Boolean((0, unknown_1.property)(item, 'italic')),
    };
}
function readColor(value) {
    if (typeof value === 'string') {
        return value;
    }
    const id = (0, unknown_1.property)(value, 'id');
    return typeof id === 'string' ? { id } : undefined;
}
//# sourceMappingURL=settings.js.map