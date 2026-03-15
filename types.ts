// types.ts

export interface ParsedData {
  id: number;
  name: string;
  description: string;
}

export interface ErrorData {
  code: number;
  message: string;
}

export type ParseResult = ParsedData | ErrorData;

export interface ParseOptions {
  filePath: string;
  delimiter: string;
}

export enum FileType {
  CSV = 'csv',
  JSON = 'json',
  XML = 'xml',
}

export interface DataParserConfig {
  fileType: FileType;
  parseOptions: ParseOptions;
}